

mums = [1,5,4,2,3,6]


def merge_sort(num):
    
    
    if len(num) <= 1:
        return num
    
    mid = len(num) // 2
    left = merge_sort(num[:mid])
    right = merge_sort(num[mid:])
    
    return merge(left, right)

def merge(left,right):
    
    l = 0
    r = 0   
    output = []
    
    while l < len(left) and r < len(right):
        
        if left[l] <= right[r]:
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1
        
    if l < len(left):
        output.extend(left[l:])
        
    if r < len(right):
        output.extend(right[r:])
    
    return output


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    m = len(nums) // 2  
    left = []
    right = []
    
    for i in range(len(nums)):
        if i == m:
            continue
        if nums[i] <= nums[m]:
            left.append(nums[i])
        
        if nums[i] > nums[m]:
            right.append(nums[i])
        
    return quick_sort(left) + [nums[m]] + quick_sort(right)
        
     