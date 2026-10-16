"""Distinct Python example #24."""
import time
capacity=3; tokens=capacity; last=time.monotonic(); rate=.5
for _ in range(5):
 now=time.monotonic(); tokens=min(capacity,tokens+(now-last)*rate);last=now; print(tokens>=1); tokens=max(0,tokens-1)
