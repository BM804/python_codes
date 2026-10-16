"""Distinct Python example #9."""
def merge_sort(a):
 if len(a)<2:return a
 m=len(a)//2; l=merge_sort(a[:m]); r=merge_sort(a[m:]); out=[]
 while l and r:out.append((l if l[0]<=r[0] else r).pop(0))
 return out+l+r
print(merge_sort([8,3,7,1,4]))
