"""Distinct Python example #27."""
def flatten(x,p=""):
 if isinstance(x,dict):return {k:v for key,value in x.items() for k,v in flatten(value,p+"."+key if p else key).items()}
 if isinstance(x,list):return {k:v for i,value in enumerate(x) for k,v in flatten(value,f"{p}[{i}]").items()}
 return {p:x}
print(flatten({"user":{"tags":["python","git"]}}))
