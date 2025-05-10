import os
import shutil
import sys
from copy_static import copy_static_files
from page_generator import generate_pages_recursive

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    output_dir = "docs"  # GitHub Pages expects the site in 'docs'

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    copy_static_files("static", output_dir)
    generate_pages_recursive("content", "template.html", output_dir, base_path)

if __name__ == "__main__":
    main()
