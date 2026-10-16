"""Distinct Python example #30."""
import re,sys
pattern=re.compile(r"^(\S+)\s+(DEBUG|INFO|WARN|ERROR)\s+(.*)$")
for line in open(sys.argv[1],encoding="utf-8"):print(pattern.match(line.strip()).groups() if pattern.match(line.strip()) else "unparsed")
