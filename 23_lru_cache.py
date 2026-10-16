"""Distinct Python example #23."""
from collections import OrderedDict
cache=OrderedDict(); cache["a"]=1; cache["b"]=2; cache.move_to_end("a"); cache["c"]=3; cache.popitem(last=False); print(cache)
