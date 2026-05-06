def cut_points(V, E):
    adj = [[] for _ in range(V + 1)]
    
    for u, v in E:
        adj[u].append(v)
        adj[v].append(u)

    visitados = [False] * (V + 1)
    disc = [0] * (V + 1)
    low = [0] * (V + 1)
    padre = [-1] * (V + 1)
    articulacion = [False] * (V + 1)

    tiempo = [0]

    def dfs(u):
        visitados[u] = True
        disc[u] = low[u] = tiempo[0]
        tiempo[0] += 1

        hijos = 0

        for v in adj[u]:
            if not visitados[v]:
                padre[v] = u
                hijos += 1
                dfs(v)

                low[u] = min(low[u], low[v])

  
                if padre[u] == -1 and hijos > 1:
                    articulacion[u] = True
                if padre[u] != -1 and low[v] >= disc[u]:
                    articulacion[u] = True

            elif v != padre[u]:
                low[u] = min(low[u], disc[v])

    for i in range(1, V + 1):
        if not visitados[i]:
            dfs(i)

    return sorted([i for i in range(1, V + 1) if articulacion[i]])


V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

print(*cut_points(V, edges))