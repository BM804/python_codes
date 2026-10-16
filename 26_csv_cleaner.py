"""Distinct Python example #26."""
import csv,sys
with open(sys.argv[1],newline="",encoding="utf-8-sig") as src, open(sys.argv[2],"w",newline="",encoding="utf-8") as dst:
 for row in csv.reader(src):
  clean=[x.strip() for x in row]
  if any(clean):csv.writer(dst).writerow(clean)
