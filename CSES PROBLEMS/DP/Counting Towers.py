
# n = int(input())
# MOD = 10**9 + 7
# dp = [[0, 0] for _ in range(n)]  

# dp[0] = [1,1]

# for i in range(1,n):
    
#     dp[i][0] = (2 * dp[i-1][0] + dp[i-1][1]) % MOD
#     dp[i][1] = (4 * dp[i-1][0] + 3 * dp[i-1][1]) % MOD
    
# print(sum(dp[-1])% MOD)

# MOD = 10**9 + 7

# # 1D
# t = int(input())
# for l in range(t):
#     n = int(input())
    
#     dp = [[0, 0] for _ in range(n)]
#     dp[0] = [1, 1]
    
#     for i in range(1, n):
#         dp[i][0] = (2*dp[i-1][0] + dp[i-1][1]) % MOD
#         dp[i][1] = (dp[i-1][0] + 4*dp[i-1][1]) % MOD
    
#     print((dp[n-1][0] + dp[n-1][1]) % MOD)
    
# 2 D

MOD = 10**9 + 7

t = int(input())
for _ in range(t):
    n = int(input())
    
    flat, zigzag = 1, 1  
    
    for i in range(1, n):
        new_flat = (2*flat + zigzag) % MOD
        new_zigzag = (flat + 4*zigzag) % MOD
        flat, zigzag = new_flat, new_zigzag
    
    print((flat + zigzag) % MOD)
