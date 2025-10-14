

n = int(input())

vals = []
for i in range(n):
    vals.append(int(input()))

def find_sums(value):
    
    summ = 0
    if value <= 9:

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
        



# Recussion: 


def sum_digits(num):
  
    num_str = str(num)
    total = 0
    for digit in num_str:
      
        total += int(digit)
    return total


def sum_all_digits(n):
    
    total = 0
    def dfs(i, running_sum):
        nonlocal total

        # base case
        if i > n:
            total = running_sum
            return

        new_sum = running_sum + sum_digits(i)

        dfs(i + 1, new_sum)

    # start recursion
    dfs(1, 0)
    return total


n = int(input())

vals = []
for i in range(n):
    vals.append(int(input()))
print(sum_all_digits(n))
