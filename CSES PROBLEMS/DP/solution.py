

n = int(input())

vals = []
for i in range(n):
    vals.append(int(input()))

    
summ = 0

max_val = max(vals)
dp = [0] * (max_val+1)
prefix = [0] * (max_val + 1)


if max_val < 10:
    print(sum(range(n + 1)))

for i in range(10):
    dp[i] = i
    
    if i > 0: 
        prefix[i] = prefix[i - 1] + i
    else:
        prefix[i] = 0
  
for i in range(10, max_val + 1):

  
    total = 0
    for ch in str(i):
        digit = int(ch) 
        total += digit
      
    dp[i] = total
    prefix[i] = prefix[i - 1] + dp[i]
    summ += dp[i]

for element in vals:
    print(prefix[element])
    
    
# O( max_vals) + 
10000
100200


200,000.00
# 0(max_val * log10(max_val))