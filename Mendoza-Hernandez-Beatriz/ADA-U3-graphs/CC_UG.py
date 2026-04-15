def dfs(node, adj, visited, comp):
    visited[node] = True
    comp.append(node)
    
    for nei in adj[node]:
        if not visited[nei]:
            dfs(nei, adj, visited, comp)


# Leer entrada
V, E = map(int, input().split())

adj = {i: [] for i in range(1, V+1)}

for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (V + 1)
components = []

# Encontrar componentes
for i in range(1, V+1):
    if not visited[i]:
        comp = []
        dfs(i, adj, visited, comp)
        comp.sort()
        components.append(comp)

# Ordenar por el primer elemento
components.sort(key=lambda x: x[0])

# Output
print(len(components))
for comp in components:
    print(*comp)