output = []

def find_kids(values):
    
    stack = []
    stack.append((values,1))
    result = []
    while stack:
        
        value, idx = stack.pop()
        max_depth = idx
        for element in value:
            
            if element.isInteger():
                result.appedn((element.getInteger(),idx))
            else:
                stack.append((element.getList(),idx+1))
    
    return result,idx

total = 0
output , max_depthhh= find_kids(nestedList)
for element in output:
    total += (element[0] * element[1])

return total


total = 0
output , max_depthhh = find_kids(nestedList)
for element in output:
    total += max_depthhh - (element[1]) + 1

return total