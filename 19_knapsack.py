"""Distinct Python example #19."""
weights=[2,3,4]; values=[4,5,6]; cap=5; dp=[0]*(cap+1)
for w,v in zip(weights,values):
 for c in range(cap,w-1,-1):dp[c]=max(dp[c],dp[c-w]+v)
print(dp[-1])
