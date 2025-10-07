

# n = int(input())

# vals = []
# for i in range(n):
#     vals.append(int(input()))

# def find_sums(value):
    
#     summ = 0
#     if value <= 9:
        
#         # print(value)
#         print(sum(range(value + 1)))
#         return
    
#     dp = [0] * (value + 1)
#     for i in range(10):
#         dp[i] = i
#         summ += i
        
#     for i in range(10,value+1):
        
#         for ch in str(i):
#             digit = int(ch)
#             dp[i] += dp[digit]
#         summ += dp[i]   
#     print(summ)
#     return
# for element in vals:
#     find_sums(element)
        

# Recussion: 

def sum_digits(num):
    """Iterative version to compute sum of digits for a single number."""
    total = 0
    while num > 0:
        total += num % 10   # take the last digit
        num //= 10          # remove the last digit
    return total



def sum_all_digits(n):
    """Recursive DFS-style function to sum all digit sums up to n."""
    res = []  # optional, just to track values (like subset)
    total = 0

    def dfs(i, running_sum):
        nonlocal total

        # base case
        if i > n:
            res.append(running_sum)
            return

        # include current number's digit sum
        new_sum = running_sum + sum_digits(i)

        # explore next value
        dfs(i + 1, new_sum)

    # start recursion
    dfs(1, 0)

    # the final accumulated sum will be stored in res[-1]
    total = res[-1] if res else 0
    return total


# Example:
n = int(input("Enter n: "))
print(sum_all_digits(n))
