import os
from pathlib import Path
from markdown_converter import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, base_path="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    output = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    output = output.replace('href="/', f'href="{base_path}')
    output = output.replace('src="/', f'src="{base_path}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(output)



def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No H1 title found in markdown.")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path="/"):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(entry_path) and entry_path.endswith(".md"):
            dest_file_path = dest_path.replace(".md", ".html")
            generate_page(entry_path, template_path, dest_file_path, base_path)

        elif os.path.isdir(entry_path):
            generate_pages_recursive(entry_path, template_path, dest_path, base_path)
