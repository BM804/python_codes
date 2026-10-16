"""Distinct Python example #18."""
from collections import deque
g={"compile":["test"],"test":["ship"],"docs":["ship"]}; nodes=set(g)|{x for v in g.values() for x in v}; d={x:sum(x in v for v in g.values()) for x in nodes}; q=deque(x for x in nodes if d[x]==0); out=[]
while q:
 u=q.popleft();out.append(u)
 for v in g.get(u,[]):d[v]-=1; q.append(v) if d[v]==0 else None
print(out)
