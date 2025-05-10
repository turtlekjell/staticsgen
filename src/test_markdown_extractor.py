import unittest
from markdown_extractor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches
        )

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "![one](url1) and ![two](url2)"
        )
        self.assertListEqual(
            [("one", "url1"), ("two", "url2")],
            matches
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "A link [here](https://example.com) and another [there](https://foo.com)"
        )
        self.assertListEqual(
            [("here", "https://example.com"), ("there", "https://foo.com")],
            matches
        )

    def test_links_ignore_images(self):
        matches = extract_markdown_links(
            "This is ![not a link](https://img.com/pic.png) but this is [a link](https://site.com)"
        )
        self.assertListEqual(
            [("a link", "https://site.com")],
            matches
        )

    def test_no_matches(self):
        self.assertListEqual([], extract_markdown_images("No images here"))
        self.assertListEqual([], extract_markdown_links("No links here"))

if __name__ == "__main__":
    unittest.main()
