"""Distinct Python example #3."""
n=int(input("n: ")); print(n>1 and all(n%d for d in range(2,int(n**.5)+1)))
