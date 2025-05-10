import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_same_values(self):
        node1 = TextNode("bold text", TextType.BOLD)
        node2 = TextNode("bold text", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq_different_text(self):
        node1 = TextNode("bold text", TextType.BOLD)
        node2 = TextNode("different text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_type(self):
        node1 = TextNode("bold text", TextType.BOLD)
        node2 = TextNode("bold text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_url(self):
        node1 = TextNode("link text", TextType.LINK, "http://example.com")
        node2 = TextNode("link text", TextType.LINK, "http://another.com")
        self.assertNotEqual(node1, node2)

    def test_eq_with_none_url(self):
        node1 = TextNode("link text", TextType.LINK)
        node2 = TextNode("link text", TextType.LINK, None)
        self.assertEqual(node1, node2)