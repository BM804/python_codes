"""Distinct Python example #33."""
from functools import wraps
import time
def retry(fn):
 @wraps(fn)
 def run(*a,**kw):
  for attempt in range(3):
   try:return fn(*a,**kw)
   except Exception:
    if attempt==2:raise
    time.sleep(.1*2**attempt)
 return run
@retry
def demo():return "success"
print(demo())
