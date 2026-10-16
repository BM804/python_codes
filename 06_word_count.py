"""Distinct Python example #6."""
from collections import Counter
print(Counter(input("Text: ").lower().split()).most_common())
