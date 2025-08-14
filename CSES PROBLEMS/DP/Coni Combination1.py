MOD = 10**9 + 7
 
num_of_coins, target = map(int, input().split())
coins = list(map(int, input().split()))
 
dp = [0] * (target + 1)
dp[0] = 1  
 
# Ordered: outer loop on sum
for current_sum in range(1, target + 1):
    for i in range(num_of_coins):
        coin = coins[i]
        if current_sum >= coin:
            dp[current_sum] = (dp[current_sum] + dp[current_sum - coin]) % MOD
 
print(dp[target])
