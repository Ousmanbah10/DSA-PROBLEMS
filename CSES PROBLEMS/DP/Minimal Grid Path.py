n = int(input())

grid = []
for i in range(n):
    row = input().strip()
    grid.append(row)

dp = []
for i in range(n):
    current = [""] * n
    dp.append(current)

dp[0][0] = grid[0][0]

# first row
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + grid[0][j]

# first column
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + grid[i][0]

# rest of the grid
for i in range(1, n):
    for j in range(1, n):
        from_top = dp[i-1][j] + grid[i][j]
        from_left = dp[i][j-1] + grid[i][j]
        if from_top < from_left:
            dp[i][j] = from_top
        else:
            dp[i][j] = from_left

print(dp[n-1][n-1])
