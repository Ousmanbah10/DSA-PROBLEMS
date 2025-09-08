import sys
n = int(input())
vals = list(map(int, input().split()))


dp = []

for i in range(len(vals)):
    current = [0]* len(vals)
    current[i] = vals[i]
    dp.append(current)

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + vals[i]



def range_sum(l, r):
    return prefix[r+1] - prefix[l]

for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        summ = range_sum(i, j)
        dp[i][j] = max(
            summ - dp[i+1][j],
            summ - dp[i][j-1]
        )


print(dp[0][n-1])
        