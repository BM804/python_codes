"""Distinct Python example #7."""
a=sorted(map(int,input("Sorted numbers: ").split())); x=int(input("Target: ")); lo,hi=0,len(a)-1
while lo<=hi:
 m=(lo+hi)//2
 if a[m]==x: break
 if a[m]<x: lo=m+1
 else: hi=m-1
print(m if lo<=hi else -1)
