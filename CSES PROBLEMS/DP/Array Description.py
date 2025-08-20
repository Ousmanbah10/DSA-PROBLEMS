

MOD = 10**9 + 7
n , m = list(map(int,input().split()))

vals = list(map(int,input().split()))

dp = [[0] * (m+2) for _ in range(n)]

if vals[0] != 0:
    dp[0][vals[0]] = 1

else:
    for v in range(1, m+1):
        dp[0][v] = 1
    
for i in range(1,n):
    
    if vals[i] != 0 : # value is not 0
        dp[i][vals[i]] = (dp[i-1][vals[i]-1] + dp[i-1][vals[i]] + dp[i-1][vals[i]+1]) % MOD
    else:
        for j in range(1,len(dp[0])-1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % MOD
            
            
ans = sum(dp[n-1]) % MOD
print(ans)
    