

# row, col, no_of_towers = map(int, input().split()) 

# from collections import deque
# from collections import defaultdict
# current = []
# for i in range(row):
#     dp = [0] * (col )
#     current.append(dp)
    


# queue = deque()
# for i in range(no_of_towers):
#     r, c = map(int, input().split())
#     current[r-1][c-1] = i + 1
#     queue.append((r-1, c-1, i + 1, 0)) 
    
    

# directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]



# closest = {}
# second = {}

# visited = set()

# while queue:
#     r, c, tower_id, dist = queue.popleft()

#     if (r, c, tower_id) in visited:
#         continue
    
#     visited.add((r, c, tower_id))
   
#     if (r, c) not in closest:
#         closest[(r, c)] = tower_id
#     elif (r, c) not in second and tower_id != closest[(r, c)]:
#         second[(r, c)] = tower_id
#     else:
#         continue
    
#     for dr, dc in directions:
#         nr, nc = r + dr, c + dc
#         if 0 <= nr < row and 0 <= nc < col:
            
            
#             existing_towers = 0
#             if (nr, nc) in closest:
#                 existing_towers += 1
#             if (nr, nc) in second:
#                 existing_towers += 1
#             if existing_towers < 2:
#                 queue.append((nr, nc, tower_id, dist + 1))
    


# closest_grid = []
# second_grid = []

# for i in range(row):
#     c_row = []
#     s_row = []
#     for j in range(col):
      
#         if (i, j) in closest:
#             c_row.append(closest[(i, j)])
#         else:
#             c_row.append(0)

      
#         if (i, j) in second:
#             s_row.append(second[(i, j)])
#         else:
#             s_row.append(0)

#     closest_grid.append(c_row)
#     second_grid.append(s_row)


# for i in range(row):
#     print(*closest_grid[i])
# for i in range(row):
#     print(*second_grid[i])


row, col, no_of_towers = map(int, input().split())
import heapq

towers = []
for i in range(no_of_towers):
    r, c = map(int, input().split())
    towers.append((r-1, c-1, i + 1))

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
closest = {}
second = {}

queue = []
for r, c, tower_id in towers:
    heapq.heappush(queue, (0, tower_id, r, c))

visited = {}

while queue:
    dist, tower_id, r, c = heapq.heappop(queue)
    
    if (r, c, tower_id) in visited:
        continue
    visited[(r, c, tower_id)] = True
    
    if (r, c) not in closest:
        closest[(r, c)] = tower_id
    elif (r, c) not in second and tower_id != closest[(r, c)]:
        second[(r, c)] = tower_id
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < row and 0 <= nc < col:
            if (nr, nc, tower_id) not in visited:
                heapq.heappush(queue, (dist + 1, tower_id, nr, nc))

closest_grid = []
second_grid = []
for i in range(row):
    c_row = []
    s_row = []
    for j in range(col):
        c_row.append(closest.get((i, j), 0))
        s_row.append(second.get((i, j), 0))
    closest_grid.append(c_row)
    second_grid.append(s_row)

for i in range(row):
    print(*closest_grid[i])
for i in range(row):
    print(*second_grid[i])