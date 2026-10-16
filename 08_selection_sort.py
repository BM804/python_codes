"""Distinct Python example #8."""
a=list(map(int,input().split()))
for i in range(len(a)):
 j=min(range(i,len(a)),key=a.__getitem__); a[i],a[j]=a[j],a[i]
print(a)
