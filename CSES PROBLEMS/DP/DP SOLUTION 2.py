

n = int(input())

vals = []
for i in range(n):
    vals.append(int(input()))
    
max_val = max(vals)

dp = [0] * (max_val + 1)
prefix = [0] * (max_val + 1)

for i in range(10):
    dp[i] = i
    if i > 0:
        prefix[i] = prefix[i - 1] + i
    else:
        prefix[i] = 0
    
for i in range(10,max_val+1):
    
    for ch in str(i):
        digit = int(ch)
        dp[i] += dp[digit]
  
    prefix[i] = prefix[i - 1] + dp[i]
    
for element in vals:
    print(prefix[element])
        
