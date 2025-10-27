

def query(l,r,array):
    
    if sum(array[l:r+1]) > 0:
        return True
    
    return False

n = int(input())


arr = list(map(int,input().strip().split()))

result = []
def find_one(l,r):
    

    if not query(l,r,arr): 
        return
    
    print(l,r,"L&R")
    if l == r:
        
        result.append(l)
        return
    
    mid = (l + r ) // 2
    find_one(l,mid)
    find_one(mid+1,r)
   
find_one(0,len(arr)-1)
print(result)