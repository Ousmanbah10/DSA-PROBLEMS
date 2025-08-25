import sys
n = int(input())

summ = 0
for i in range(1,n+1):
    summ += i
   
MOD = 10 ** 9 + 7

dp = []

if summ % 2 != 0:
    print(0)
    sys.exit()

v = (summ // 2 + 1)
for  i in range(n+1):
    current = [0] * v
    dp.append(current)


dp[0][0] = 1

for i in range(1,n+1):
    
    for j in range(v):
    
        if j >= i:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-i]) % MOD
        else:
            dp[i][j] = dp[i-1][j]
        
ans = dp[n][summ // 2]
ans = (ans * pow(2, MOD-2, MOD)) % MOD   
print(ans)
        