from htmlnode import ParentNode, LeafNode
from block_parser import markdown_to_blocks
from block_classifier import block_to_block_type
from block_type import BlockType
from text_parser import text_to_textnodes
from textnode_to_html import text_node_to_html_node
from textnode import TextNode, TextType

def text_to_children(text):
    return [text_node_to_html_node(node) for node in text_to_textnodes(text)]

def paragraph_to_html(block):
    return ParentNode("p", text_to_children(block))

def heading_to_html(block):
    heading_level = len(block.split(" ")[0])  # e.g. "### Title" → 3
    tag = f"h{heading_level}"
    text = block[heading_level+1:].strip()  # skip the #s and space
    return ParentNode(tag, text_to_children(text))

def quote_to_html(block):
    stripped = "\n".join([line[1:].strip() for line in block.split("\n")])
    return ParentNode("blockquote", text_to_children(stripped))

def unordered_list_to_html(block):
    items = block.split("\n")
    li_nodes = [ParentNode("li", text_to_children(item[2:].strip())) for item in items]
    return ParentNode("ul", li_nodes)

def ordered_list_to_html(block):
    items = block.split("\n")
    li_nodes = [ParentNode("li", text_to_children(item.split(". ", 1)[1].strip())) for item in items]
    return ParentNode("ol", li_nodes)

def code_block_to_html(block):
    code_text = "\n".join(block.split("\n")[1:-1]) + "\n"  # remove triple backticks
    return ParentNode("pre", [LeafNode("code", code_text)])


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            html_blocks.append(paragraph_to_html(block))
        elif block_type == BlockType.HEADING:
            html_blocks.append(heading_to_html(block))
        elif block_type == BlockType.QUOTE:
            html_blocks.append(quote_to_html(block))
        elif block_type == BlockType.UNORDERED_LIST:
            html_blocks.append(unordered_list_to_html(block))
        elif block_type == BlockType.ORDERED_LIST:
            html_blocks.append(ordered_list_to_html(block))
        elif block_type == BlockType.CODE:
            html_blocks.append(code_block_to_html(block))

    return ParentNode("div", html_blocks)
