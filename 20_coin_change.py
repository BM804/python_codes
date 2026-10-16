"""Distinct Python example #20."""
coins=[1,3,4]; amount=6; dp=[0]+[999]*amount
for x in range(1,amount+1):dp[x]=min([dp[x-c]+1 for c in coins if c<=x] or [999])
print(dp[amount] if dp[amount]<999 else None)
