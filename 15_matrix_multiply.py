"""Distinct Python example #15."""
a=[[1,2],[3,4]]; b=[[5,6],[7,8]]; print([[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))])
