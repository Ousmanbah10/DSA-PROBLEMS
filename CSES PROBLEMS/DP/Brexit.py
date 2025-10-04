from collections import deque
from collections import defaultdict


numberOfNodes, numberOfConnections, home, leaving = map(int, input().split())

graph = defaultdict(list)
initialConnection = defaultdict(int)
originalConnection = {}  


for i in range(numberOfConnections):
    n, b = map(int, input().split())
    graph[n].append(b)
    graph[b].append(n)
    initialConnection[n] += 1
    initialConnection[b] += 1


originalConnection = initialConnection.copy()


queue = deque([leaving])
visited = set()
visited.add(leaving)

while queue:
    node = queue.popleft()  # Correct FIFO queue behavior for BFS
    
    for element in graph[node]:
        if element in visited:
            continue  # Skip already processed nodes
        
        # Reduce the trade connection count of the neighboring country
        initialConnection[element] -= 1  

        # Check if the country now has less than half of its original trade connections
        if initialConnection[element] * 2 <= originalConnection[element]:  
            queue.append(element)
            visited.add(element)

# Output the result based on whether home was visited
if home in visited:
    print("leave")
else:
    print("stay")
