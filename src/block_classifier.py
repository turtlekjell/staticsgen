from block_type import BlockType

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if len(lines) == 1 and lines[0].startswith("#"):
        hashes, _, rest = lines[0].partition(" ")
        if 1 <= len(hashes) <= 6 and all(c == "#" for c in hashes):
            return BlockType.HEADING

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(
        line.lstrip().startswith(f"{i}. ")
        for i, line in enumerate(lines, start=1)
    ):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
