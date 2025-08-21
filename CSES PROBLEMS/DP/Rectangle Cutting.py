
a , b = map(int,input().split())


dp  = []

for i in range(a+1):
    current = [0] * (b + 1)
    dp.append(current)


for j in range(1, b+1):
    dp[1][j] = j - 1
    
for i in range(1, a+1):
    dp[i][1] = i - 1
    
for i in range(2,a+1):
    for j in range(2,b+1):
        
        if i == j:
            dp[i][j] = 0
        else:
            best = float('inf')
           
            for k in range(1, i):
                best = min(best, dp[k][j] + dp[i-k][j] + 1)
          
            for k in range(1, j):
                best = min(best, dp[i][k] + dp[i][j-k] + 1)
            dp[i][j] = best
print(dp[-1][-1])