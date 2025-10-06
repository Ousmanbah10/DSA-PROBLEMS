

n = int(input())

vals = []
for i in range(n):
    vals.append(int(input()))

def find_sums(value):
    
    summ = 0
    if value <= 9:
        
        # print(value)
        print(sum(range(value + 1)))
        return
    
    dp = [0] * (value + 1)
    for i in range(10):
        dp[i] = i
        summ += i
        
    for i in range(10,value+1):
        
        for ch in str(i):
            digit = int(ch)
            dp[i] += dp[digit]
        summ += dp[i]   
    print(summ)
    return

for element in vals:
    find_sums(element)
        

