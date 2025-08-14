MOD = 10**9 + 7
 
num_of_coins, target = map(int, input().split())
coins = list(map(int, input().split()))
 
 
dp = []
for i in range(num_of_coins + 1):
    row = [0] * (target + 1)
    row[0] = 1 
    dp.append(row)
 
 
for i in range(1, num_of_coins + 1):  
    coin = coins[i - 1]
    for j in range(1, target + 1):  
        if j < coin:
            dp[i][j] = dp[i - 1][j]  
        else:
           
            dp[i][j] = (dp[i - 1][j] + dp[i][j - coin]) % MOD
 
print(dp[num_of_coins][target])