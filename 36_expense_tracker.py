"""Distinct Python example #36."""
import csv
from collections import defaultdict
sums=defaultdict(float)
try:
 for row in csv.DictReader(open("expenses.csv",newline="")):sums[row["category"]]+=float(row["amount"])
 print(dict(sums))
except FileNotFoundError:print("Add rows to expenses.csv first")
