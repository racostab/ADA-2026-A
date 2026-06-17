nmw = input().split()
n = int(nmw[0])
m = int(nmw[1])
t = int(nmw[2]) if len(nmw) > 2 else 1

graph = [[] for _ in range(n + 1)]
INF = 1000000000

def dijkstra(n, graph, source):
    #inicializamos lista de distancias y de visitados
    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    dist[source] = 0

    for _ in range(n):
        #buscamos el nodo no visitado que tenga menor distancia
        u = -1
        for v in range(1, n + 1):
            if not visited[v]:
                if u == -1 or dist[v] < dist[u]:
                    u = v

        if dist[u] == INF:
            break

        #marcamos el nodo ya visitado
        visited[u] = True

        #recorermos los vecinos
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

for _ in range(m):
    abw = input().split()
    a = int(abw[0])
    b = int(abw[1])
    w = int(abw[2])
    graph[a].append((b,w))
    graph[b].append((a,w))

result = dijkstra(n,graph,1)

print(" ".join(str(result[i]) for i in range(2, n + 1)))