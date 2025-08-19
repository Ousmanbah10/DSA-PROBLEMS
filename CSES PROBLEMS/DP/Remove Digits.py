import sys
n = int(input())

dp = [float("inf")] * (n+1)
dp[0] = 0

if n <= 9:
    print(1)
    sys.exit()
for i in range(1,10):
    
    dp[i] = 1

val = 0
for i in range(10,n+1):
    
    for element in str(i):
    
        d = int(element)
        if d > 0:
            val = i - d
            dp[i] = min(dp[i],dp[val]+1)
print(dp[-1])