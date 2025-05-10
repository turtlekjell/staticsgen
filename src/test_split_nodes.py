import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    def test_split_code(self):
        input_node = TextNode("Text with `code` example", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "`", TextType.CODE)
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" example", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_bold(self):
        input_node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_italic(self):
        input_node = TextNode("This is _italic_ text", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_nodes_mixed(self):
        input_nodes = [
            TextNode("This is _italic_", TextType.TEXT),
            TextNode(" and not touched", TextType.CODE),
        ]
        result = split_nodes_delimiter(input_nodes, "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and not touched", TextType.CODE),
        ]
        self.assertEqual(result, expected)


    def test_unmatched_delimiter(self):
        input_node = TextNode("This is _broken markdown", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([input_node], "_", TextType.ITALIC)
        self.assertIn("Invalid markdown", str(context.exception))

if __name__ == "__main__":
    unittest.main()
