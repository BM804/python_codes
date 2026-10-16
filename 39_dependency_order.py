"""Distinct Python example #39."""
graph={"app":["ui","db"],"ui":["http"],"db":["http"]}; seen=set(); order=[]
def visit(n):
 if n not in seen:
  seen.add(n)
  for d in graph.get(n,[]):visit(d)
  order.append(n)
visit("app"); print(order[:-1])
