"""Distinct Python example #40."""
import base64,json
parts=input("JWT: ").split(".")
if len(parts)!=3:raise ValueError("Expected 3 sections")
print(json.loads(base64.urlsafe_b64decode(parts[1]+"="*(-len(parts[1])%4))))
