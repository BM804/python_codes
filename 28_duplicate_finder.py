"""Distinct Python example #28."""
from pathlib import Path
from hashlib import sha256
from collections import defaultdict
import sys
found=defaultdict(list)
for p in Path(sys.argv[1] if len(sys.argv)>1 else ".").rglob("*"):
 if p.is_file():found[sha256(p.read_bytes()).hexdigest()].append(p)
print([v for v in found.values() if len(v)>1])
