

n = int(input())

vals = []
for i in range(n):
    vals.append(int(input()))

def find_sums(value):
    
    sum = 0
    if value <= 9:
        
        print(value)
        return
    
    dp = [0] * (value + 1)
    for i in range(10):
        dp[i] = i
        sum += i
        
    for i in range(10,value+1):
        
        for ch in str(i):
            digit = int(ch)
            dp[i] += dp[digit]
        sum += dp[i]   
    print(sum)
    return
for element in vals:
    find_sums(element)
        

