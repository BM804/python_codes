"""Find files with identical contents using streaming SHA-256 hashes."""
from collections import defaultdict
from hashlib import sha256
from pathlib import Path
import sys

def find_duplicates(root: Path):
    by_hash = defaultdict(list)
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        digest = sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        by_hash[digest.hexdigest()].append(path)
    return [paths for paths in by_hash.values() if len(paths) > 1]

if __name__ == "__main__":
    folder = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    for group in find_duplicates(folder):
        print("Duplicate files:")
        for path in group:
            print(f"  {path}")
