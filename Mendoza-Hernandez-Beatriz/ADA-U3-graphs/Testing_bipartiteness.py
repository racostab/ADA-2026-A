from collections import deque

# Read number of vertices and edges
V, E = map(int, input().split())

# Adjacency list
graph = [[] for _ in range(V + 1)]

# Read edges
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# -1 = unvisited
# 0 = set U
# 1 = set V
color = [-1] * (V + 1)

# BFS to check bipartite graph
queue = deque()
queue.append(1)
color[1] = 0

is_bipartite = True

while queue and is_bipartite:
    node = queue.popleft()

    for neighbor in graph[node]:

        # If unvisited, assign opposite color
        if color[neighbor] == -1:
            color[neighbor] = 1 - color[node]
            queue.append(neighbor)

        # Same color means not bipartite
        elif color[neighbor] == color[node]:
            is_bipartite = False
            break

# Output result
if not is_bipartite:
    print("EMPTY")
else:
    U = []
    V_set = []

    for i in range(1, V + 1):
        if color[i] == 0:
            U.append(i)
        else:
            V_set.append(i)

    print(*sorted(U))
    print(*sorted(V_set))