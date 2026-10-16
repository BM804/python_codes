"""Distinct Python example #31."""
import re
p=input("Password: "); checks=[len(p)>=12,bool(re.search("[a-z]",p)),bool(re.search("[A-Z]",p)),bool(re.search(r"\d",p)),bool(re.search(r"\W",p))]; print(sum(checks),"/5")
