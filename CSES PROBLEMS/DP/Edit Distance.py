first_str = input().strip()
second_str = input().strip()

max_len = len(first_str)
min_len = len(second_str)

dp = []
for i in range(max_len + 1):
    row = []
    for j in range(min_len + 1):
        row.append(0)
    dp.append(row)

for i in range(max_len + 1):
    dp[i][0] = i
for j in range(min_len + 1):
    dp[0][j] = j

for i in range(1, max_len + 1):
    for j in range(1, min_len + 1):
        if first_str[i - 1] == second_str[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(
                dp[i - 1][j],
                dp[i][j - 1],
                dp[i - 1][j - 1]
            )

print(dp[max_len][min_len])
