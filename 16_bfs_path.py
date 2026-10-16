"""Distinct Python example #16."""
from collections import deque
g={"A":["B","C"],"B":["D"],"C":["D"],"D":[]}; q=deque(["A"]); prev={"A":None}
while q:
 u=q.popleft()
 for v in g[u]:
  if v not in prev:prev[v]=u;q.append(v)
node="D"; path=[]
while node is not None:path.append(node);node=prev[node]
print(path[::-1])
