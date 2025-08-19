


n , m = list(map(int,input().split()))

print(n,m)

vals = list(map(int,input().split()))

dp = [[0] * (m+2) for _ in range(n+1)]

if vals[0] != 0:
    dp[0][vals[0]] = 1
else:
    dp[0][1] = 1
    
for i in range(1,n):
    
    
    
    if vals[i] != 0: # value is not 0 
        dp[i][vals[i]] += dp[i-1][vals[i]-1]
        dp[i][vals[i]] += dp[i-1][vals[i]]
        dp[i][vals[i]] += dp[i-1][vals[i]+1]
        
    print("hh")
    
    for j in range(1,len(dp[0])-1):
        
        if dp[i-1][j] > 0:
            dp[i][j-1] += 1 # prev
            dp[i][j] += 1 #current
            dp[i][j+1] += 1 # next
print(dp)
    