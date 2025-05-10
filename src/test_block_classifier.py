import unittest
from block_classifier import block_to_block_type
from block_type import BlockType

class TestBlockClassifier(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# Heading 1"),
            BlockType.HEADING,
        )
        self.assertEqual(
            block_to_block_type("### Heading 3"),
            BlockType.HEADING,
        )

    def test_code_block(self):
        code = "```\ndef hello():\n    return 'hi'\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote_block(self):
        block = "> line one\n> line two\n> quote again"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- item one\n- item two\n- item three"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "This is a normal paragraph\nwith multiple lines."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_mixed_list_should_be_paragraph(self):
        block = "1. Item one\n- item two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
