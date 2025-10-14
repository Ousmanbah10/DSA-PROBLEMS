
        
import sys
from collections import deque

row, col = map(int, input().split())
start_i, start_j = map(int, input().split())
end_i, end_j = map(int, input().split())

maze = []
for i in range(row):
    maze.append(input().strip())


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


start_r, start_c = start_i - 1, start_j - 1
end_r, end_c = end_i - 1, end_j - 1


queue = deque()
queue.append((start_r, start_c, 0))

visited_states = set()

while queue:
    curr_r, curr_c, direction_idx = queue.popleft()
    
    if (curr_r, curr_c) == (end_r, end_c):
        print(1)
        exit()
    
    # Check for loop
    state = (curr_r, curr_c, direction_idx)
    if state in visited_states:
        continue
    
    visited_states.add(state)
    
   
    dr, dc = directions[direction_idx]
    
    # turn left
    left_idx = (direction_idx - 1) % 4
    left_dr, left_dc = directions[left_idx]
    left_r, left_c = curr_r + left_dr, curr_c + left_dc
    
    if (0 <= left_r < row and 0 <= left_c < col and 
        maze[left_r][left_c] == '0'):
   
        queue.append((left_r, left_c, left_idx))
    else:
   
        forward_r, forward_c = curr_r + dr, curr_c + dc
        
        if (0 <= forward_r < row and 0 <= forward_c < col and 
            maze[forward_r][forward_c] == '0'):
       
            queue.append((forward_r, forward_c, direction_idx))
        else:
            
            queue.append((curr_r, curr_c, (direction_idx + 1) % 4))


print(0)



#4 5
# 1 1
# 4 5
# 00111
# 10100
# 10111
# 10000