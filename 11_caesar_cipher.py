"""Distinct Python example #11."""
text=input(); shift=int(input()); print("".join(chr((ord(c)-97+shift)%26+97) if c.islower() else c for c in text))
