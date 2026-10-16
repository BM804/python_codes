"""Distinct Python example #29."""
import re,sys
p=Path(sys.argv[1]) if False else None
text=open(sys.argv[1],encoding="utf-8").read()
for target in re.findall(r"!?\[[^]]*\]\(([^)]+)\)",text):
 if "://" not in target and target and not __import__("os").path.exists(target.split("#")[0]):print("missing",target)
