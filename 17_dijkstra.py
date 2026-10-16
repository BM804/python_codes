"""Distinct Python example #17."""
import heapq
g={"A":[("B",4),("C",1)],"C":[("B",2)],"B":[]}; d={"A":0}; q=[(0,"A")]
while q:
 cost,u=heapq.heappop(q)
 if cost!=d[u]:continue
 for v,w in g[u]:
  if cost+w<d.get(v,999):d[v]=cost+w;heapq.heappush(q,(d[v],v))
print(d)
