import sys
n = int(input())
vals = list(map(int, input().split()))

if n == 1:
    print(1)
    sys.exit()

dp = [float("inf")]* n

dp[0] = 1
start = vals[0]
maxx = float("-inf")
for i in range(1,n):
    
    
    if start > vals[i]:
        dp[i] = dp[i-1] + 1
    else:
        start = vals[i]
        dp[i]= 1
    maxx = max(dp[i],maxx)
print(maxx)
    