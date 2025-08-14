from collections import defaultdict
 
n = int(input())
dict = defaultdict(int)
 
MOD = 10**9 + 7
# output = []
# for i in range(n+1):
 
#     current = [0]* (6)
#     output.append(current)
# dict[0] = 1
 
# for i in range(1,n+1):
#     count = 0
#     for j in range(1,7):
        
#         if i - j >= 0:
            
#             output[i][j-1] = dict[i - j]
#             count += (output[i][j-1] % MOD)
        
#     dict[i] = count
    
dp = [0]*(n+1)
dp[0] = 1
 
for i in range(1, n+1):
    total = 0
    for j in range(1, 7):              
        if i - j >= 0:
            # output[i][j-1] = dp[i - j]   # optional grid fill
            total = (total + dp[i - j]) % MOD
    dp[i] = total
 
print(dp[n])
# print(dict[n])
        