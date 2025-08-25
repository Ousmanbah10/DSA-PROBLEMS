

n = int(input())

vals = list(map(int, input().split()))
sum_vals = sum(vals)
x = len(vals)
dp = []

for i in range(x+1):
    
    current = [0] * (sum_vals+1)
    dp.append(current)
    

dp[0][0] = 1
for i in range(n+1):
    dp[i][0] = 1

for i in range(1,x+1):
    
    for j in range(1,sum_vals+1):
        
        
        if j < vals[i-1] or dp[i-1][j] == 1:
            dp[i][j] = dp[i-1][j]
        else:
            value = j - vals[i - 1]
       
            dp[i][j] = dp[i-1][value]

count = 0
out = []
for i in range(1,sum_vals+1):
    if dp[-1][i] == 1:
        out.append(i)
        
print(len(out))

for val in out:
    print(val, end=" ")
