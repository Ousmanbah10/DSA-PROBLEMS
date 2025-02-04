'''
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

def numIslands2( m: int, n: int, positions) :

    if len(positions) == 0:
        return []
    if len(positions) == 1:
        return [1]    

    class UnionFind:

        def __init__ (self,size):
            self.par = list(range(size))
            self.rank = [1] * size

        def find(self, x):

            if self.par[x] != x:
                self.par[x] = self.find(self.par[x])
            return self.par[x]

        def union(self, x, y):

            p1 = self.find(x)
            p2 = self.find(y)

            if p1 == p2:
                return False

            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
                self.rank[p1] += self.rank[p2]
            else:
                self.par[p1] = p2
                self.rank[p2] += self.rank[p1]

            return True          

    array = [0] * len(positions)
    dict = {} 
    visited = set()
    uf = UnionFind(len(positions))
    array[0] = 1

    
    dict[(positions[0][0], positions[0][1])] = 0
    visited.add((positions[0][0], positions[0][1]))

    val = 1

    for i, value in enumerate(positions[1:], start=1):  
        
        if (value[0], value[1]) in visited:
            array[i] = val  
            continue

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        mini_set = set()
        current = []

        for element in directions:
            dr, dc = element
            neighbor = (value[0] + dr, value[1] + dc)

            
            if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n and neighbor in dict:
                current.append(dict[neighbor])
                mini_set.add(uf.find(dict[neighbor]))

        dict[(value[0], value[1])] = i
        visited.add((value[0], value[1]))
        if len(mini_set) == 1:
            
            for neighbor_index in current:
                uf.union(i, neighbor_index)
            array[i] = val


        
        elif len(mini_set) > 1:
            

            min_set = set()
            for neighbor_index in current:
                # **CHANGED**: Use `uf.find` to get the unique parent of each neighbor
                parent = uf.find(neighbor_index)
                min_set.add(parent)  # Add unique parents to min_set
                uf.union(i, neighbor_index)  # Union current with neighbors

            # **CHANGED**: Subtract based on the size of `min_set`
            val -= (len(min_set) - 1)
            val = max(1, val)  # Ensure val stays valid
            array[i] = val




        elif len(mini_set) == 0:
            
            val += 1
            array[i] = val

        
        

    return array  

positions = [[0,0],[0,1],[1,2],[2,1]]


print( numIslands2(3,3, positions))