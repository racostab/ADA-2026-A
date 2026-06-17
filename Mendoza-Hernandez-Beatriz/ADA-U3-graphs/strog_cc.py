from collections import defaultdict
import sys

data = list(map(int, sys.stdin.read().split()))

if not data:
    sys.exit()

V, E = data[0], data[1]

graph = defaultdict(list)
rev_graph = defaultdict(list)

idx = 2

for _ in range(E):
    u = data[idx]
    v = data[idx + 1]
    idx += 2

    graph[u].append(v)
    rev_graph[v].append(u)

visited = set()
order = []

# Primer DFS
def dfs1(u):
    visited.add(u)

    for v in graph[u]:
        if v not in visited:
            dfs1(v)

    order.append(u)

for vertex in range(1, V + 1):
    if vertex not in visited:
        dfs1(vertex)

# Segundo DFS sobre el grafo transpuesto
visited.clear()
sccs = []

def dfs2(u, component):
    visited.add(u)
    component.append(u)

    for v in rev_graph[u]:
        if v not in visited:
            dfs2(v, component)

for vertex in reversed(order):
    if vertex not in visited:
        component = []
        dfs2(vertex, component)

        component.sort()
        sccs.append(component)

# Ordenar componentes por su primer elemento
sccs.sort(key=lambda x: x[0])

print(len(sccs))

for comp in sccs:
    print(*comp)