def markdown_to_blocks(markdown):
    # Split on double newlines
    raw_blocks = markdown.split("\n\n")

    # Strip whitespace and remove empty blocks
    blocks = [block.strip() for block in raw_blocks if block.strip() != ""]

    return blocks
