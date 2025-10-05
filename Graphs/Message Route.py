from collections import deque

n, m = map(int, input().split())

adj = []
for i in range(n + 1):
    adj.append([])

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

parent = [-1] * (n + 1)
queue = deque()
queue.append(1)
parent[1] = 0  # mark as visited

while len(queue) > 0:
    u = queue.popleft()
    if u == n:
        break
    for v in adj[u]:
        if parent[v] == -1:
            parent[v] = u
            queue.append(v)

if parent[n] == -1:
    print("IMPOSSIBLE")
else:
    path = []
    cur = n
    while cur != 0:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    print(len(path))
    for node in path:
        print(node, end=" ")
    print()

