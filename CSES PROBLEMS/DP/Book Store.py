

#2D APPROACH
import sys

n, x = map(int, input().split())

vals = list(map(int, input().split()))
pages = list(map(int,input().split()))


dp = [[0] * (x + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    v = i - 1  # index in vals/pages
    for j in range(x + 1):
        if vals[v] > j:
            dp[i][j] = dp[i-1][j]  # can't take book
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - vals[v]] + pages[v])  # take or skip

print(dp[-1][-1])

# 1D Approach
n, x = map(int, input().split())

vals = list(map(int, input().split()))
pages = list(map(int, input().split()))

dp = [0] * (x + 1)

for i in range(1, n + 1):
    v = i - 1
    for j in range(x, -1, -1):
        if vals[v] > j:
            continue
        else:
            dp[j] = max(dp[j], dp[j - vals[v]] + pages[v])

print(dp[x])


