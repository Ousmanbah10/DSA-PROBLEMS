n = int(input())
a = list(map(int, input().split()))
s = list(map(int, input().split()))


s.sort(reverse=True)

max_average = 0.0

for k in range(1, n + 1):
 
    skill_sum = sum(s[:k])
    
  
    total_problems = skill_sum + a[k - 1]
    

    average = total_problems / k
    

    max_average = max(max_average, average)

print(max_average)

#2
# 283663485 732616075
# 0 93763082


#1
# 17109549
# 100000000