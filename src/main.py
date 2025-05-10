import os
import shutil
from copy_static import copy_static_files
from page_generator import generate_page

from page_generator import generate_pages_recursive

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_static_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")

'''
def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_static_files("static", "public")

    for root, _, files in os.walk("content"):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                # Determine output path
                rel_path = os.path.relpath(from_path, "content")
                dest_path = os.path.join("public", rel_path)
                dest_path = dest_path.replace(".md", ".html")
                generate_page(from_path, "template.html", dest_path)
'''
if __name__ == "__main__":
    main()
