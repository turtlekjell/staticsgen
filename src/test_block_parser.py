import unittest
from block_parser import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_leading_and_trailing_newlines(self):
        md = """\n\n\nThis is block one\n\n\nThis is block two\n\n"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is block one", "This is block two"])

    def test_only_whitespace_blocks(self):
        md = """Line 1

   
Line 2"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Line 1", "Line 2"])

    def test_single_block(self):
        md = "No newlines here"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["No newlines here"])

if __name__ == "__main__":
    unittest.main()
