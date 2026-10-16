"""Distinct Python example #10."""
n=int(input("n: ")); a,b=0,1
for _ in range(n):a,b=b,a+b
print(a)
