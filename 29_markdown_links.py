"""Report broken relative links in a Markdown document."""
from pathlib import Path
import re
import sys

LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

def broken_links(markdown_file: Path) -> list[str]:
    text = markdown_file.read_text(encoding="utf-8")
    missing = []
    for raw_target in LINK_PATTERN.findall(text):
        target = raw_target.strip().split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        if not (markdown_file.parent / target).exists():
            missing.append(raw_target.strip())
    return missing

if __name__ == "__main__":
    path = Path(sys.argv[1])
    for target in broken_links(path):
        print("Missing:", target)
