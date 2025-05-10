import unittest
from page_generator import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_normal(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_extract_title_stripped(self):
        self.assertEqual(extract_title("#     Hello World   "), "Hello World")

    def test_extract_title_first_heading(self):
        md = "# Title One\n\n## Subtitle"
        self.assertEqual(extract_title(md), "Title One")

    def test_extract_title_raises(self):
        md = "## No top-level heading here"
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()
