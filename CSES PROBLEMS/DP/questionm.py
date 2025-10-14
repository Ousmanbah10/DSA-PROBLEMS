

people, egdes = map(int, input().split())

from collections import defaultdict, deque

graph = defaultdict(list)

for i in range(egdes):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  

print(graph)

for key in graph:
    if key

