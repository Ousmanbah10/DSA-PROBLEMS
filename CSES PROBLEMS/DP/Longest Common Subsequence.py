n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

from collections import defaultdict
dict = defaultdict(int)


dp = []
longStr = a
shortStr = b

str1 = a
str2 = b
seen = set()
res = []


for i in range(len(str2) + 1):
    current = [0] * (len(str1) + 1)
    dp.append(current)

# Fill the DP table
for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
    
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

i, j = len(str2), len(str1)
while i > 0 and j > 0:
    if str2[i-1] == str1[j-1]:
        res.append(str(str2[i-1]))
        i -= 1
        j -= 1
    elif dp[i-1][j] >= dp[i][j-1]:
        i -= 1
    else:
        j -= 1

res.reverse()


print(dp[-1][-1])
print(" ".join(res))

