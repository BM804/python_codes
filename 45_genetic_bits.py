"""Distinct Python example #45."""
import random
rng=random.Random(3); pop=[[rng.randrange(2) for _ in range(16)] for _ in range(30)]
for _ in range(80):
 pop.sort(key=sum,reverse=True)
 if sum(pop[0])==16:break
 parents=pop[:10]; nxt=parents[:2]
 while len(nxt)<30:
  a,b=rng.sample(parents,2);cut=rng.randrange(1,16);child=a[:cut]+b[cut:];i=rng.randrange(16)
  if rng.random()<.05:child[i]^=1
  nxt.append(child)
 pop=nxt
print("".join(map(str,max(pop,key=sum))))
