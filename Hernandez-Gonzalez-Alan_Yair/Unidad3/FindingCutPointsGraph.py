from collections import defaultdict

ve = input().split()
v = int(ve[0])
e = int(ve[1])

graph = defaultdict(list)


for _ in range(e):
    uv = input().split()
    u, v = int(uv[0]), int(uv[1])
    graph[u].append(v)
    graph[v].append(u)    



def dfs(u, parent, graph, visited, disc, low, is_cut, timer):
    visited.add(u)
    disc[u] = low[u] = timer[0]
    timer[0] += 1
    children = 0

    for v in graph[u]:
        if v not in visited:
            children += 1
            dfs(v, u, graph, visited, disc, low, is_cut, timer)

            low[u] = min(low[u], low[v])

            # nodo interno
            if parent != -1 and low[v] >= disc[u]:
                is_cut.add(u)

            # raíz con 2 hijos
            if parent == -1 and children > 1:
                is_cut.add(u)

        elif v != parent:
            low[u] = min(low[u], disc[v])


visited = set()
disc    = {}
low     = {}
is_cut  = set()
timer   = [0]

for i in range(1, v + 1):
    if i not in visited:
        dfs(i, -1, graph, visited, disc, low, is_cut, timer)

print(" ".join(str(v) for v in sorted(is_cut)))