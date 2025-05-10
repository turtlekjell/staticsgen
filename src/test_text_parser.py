import unittest
from text_parser import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_full_conversion(self):
        input_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        result = text_to_textnodes(input_text)
        self.assertListEqual(result, expected)

    def test_empty_string(self):
        self.assertListEqual(text_to_textnodes(""), [])

    def test_text_only(self):
        input_text = "Just a plain sentence."
        expected = [TextNode("Just a plain sentence.", TextType.TEXT)]
        self.assertListEqual(text_to_textnodes(input_text), expected)

    def test_code_only(self):
        input_text = "`monospaced`"
        expected = [TextNode("monospaced", TextType.CODE)]
        self.assertListEqual(text_to_textnodes(input_text), expected)

if __name__ == "__main__":
    unittest.main()
