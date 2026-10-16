"""Distinct Python example #22."""
from collections import deque
maze=["...",".#.","..."]; start=(0,0); goal=(2,2); q=deque([start]); prev={start:None}
while q:
 r,c=q.popleft()
 for y,x in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
  if 0<=y<3 and 0<=x<3 and maze[y][x]!="#" and (y,x) not in prev:prev[(y,x)]=(r,c);q.append((y,x))
print(prev.get(goal))
