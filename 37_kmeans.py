"""Distinct Python example #37."""
from math import dist
points=[(1,2),(2,1),(8,9),(9,8)]; centers=points[::3]
for _ in range(10):
 groups=[[] for _ in centers]
 for p in points:groups[min(range(len(centers)),key=lambda i:dist(p,centers[i]))].append(p)
 centers=[tuple(sum(p[d] for p in g)/len(g) for d in (0,1)) for g in groups]
print(centers)
