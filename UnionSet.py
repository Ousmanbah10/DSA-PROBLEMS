class UnionSet:
    
    def __init__(self,n):
        
        self.array = [-1] * n
        self.rank = [1] * n
        
    def find(self,x):
        
        if self.array[x] == -1:
            return x
        
        parent = self.array[x]
        
        while self.array[parent] != -1:
            parent = self.array[parent]
        return parent

    def union(self,x,y):
        
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y: 
            return
        
        rank_x = self.rank[parent_x]
        rank_y = self.rank[parent_y]
        
        if self.rank_y > self.rank_x:
            self.array[parent_x] = parent_y
            self.rank[y] += self.rank[x]
        else:
            self.array[parent_y] = parent_x
            self.rank[x] += self.rank[y]
        