import re

def extract_markdown_images(text):
    # Match ![alt](url)
    pattern = r'!\[(.*?)\]\((.*?)\)'
    return re.findall(pattern, text)

def extract_markdown_links(text):
    # Match [text](url), but not images (skip if preceded by '!')
    pattern = r'(?<!\!)\[(.*?)\]\((.*?)\)'
    return re.findall(pattern, text)
