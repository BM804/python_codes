"""Distinct Python example #4."""
import math
a,b=map(int,input().split()); print(math.gcd(a,b), abs(a*b)//math.gcd(a,b) if a*b else 0)
