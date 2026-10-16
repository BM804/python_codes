"""Distinct Python example #21."""
grid=[[((r*3+r//3+c)%9)+1 for c in range(9)] for r in range(9)]; expected=set(range(1,10)); print(all(set(row)==expected for row in grid))
