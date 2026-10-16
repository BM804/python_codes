"""Distinct Python example #5."""
import re
s=re.sub(r"[^a-z0-9]","",input().lower()); print(s==s[::-1])
