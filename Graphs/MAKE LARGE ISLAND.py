class Solution:
    def largestIsland(self, grid) -> int:
        
        n = len(grid)
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

        row = len(grid)
        col = len(grid[0])
        uf = UnionFind(n * n)
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
       
        zeros = set()
        
        def bfs(i,j):

            queue = deque()
            queue.append((i,j))
            size = 0
            visited.add((i,j))
            while queue:

                rr, cc = queue.popleft()
              
                n_idx = (n * rr) + cc

                for dr, dc in directions:
                    nd, nc = rr + dr, cc + dc
                    
                    if 0 <= nd < row and 0 <= nc < col and grid[nd][nc] and (nd,nc) not in visited:
                        n_idxxx = (n * nd) + nc
                        if grid[nd][nc] == 1:
                            uf.union(n_idx,n_idxxx)
                            queue.append((nd,nc))
                            visited.add((nd,nc))
  
                    
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs(i,j)
                elif grid[i][j] == 0:
                    zeros.add((i,j))
        
                    
        print(uf.par)

        island_size = defaultdict(int)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    root = uf.find(r * n + c)
                    island_size[root] += 1

        max_island = max(island_size.values(), default=0)

       
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    total = 1  # start with 1 for the flipped cell
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            root = uf.find(nr * n + nc)
                            if root not in seen:
                                seen.add(root)
                                total += island_size[root]
                    max_island = max(max_island, total)

        return max_island if max_island != 0 else n * n