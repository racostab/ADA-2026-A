X = input().split()
if len(X) == 3:
    V = int(X[0])
    M = int(X[1])
    T = int(X[2])
else:
    V = int(X[0])
    M = int(X[1])
    T = None

grafo = {v: [] for v in range(1, V + 1)}

for _ in range(M):
    u, v, w = map(int, input().split())
    grafo[u].append((v, w))


dist = {v: float('inf') for v in range(1, V + 1)}
dist[1] = 0
visitados = []
previo = {v: None for v in range(1, V + 1)}



while len(visitados) < V:
    nodos_no_visitados = [v for v in range(1, V + 1) if v not in visitados]
    u = min(nodos_no_visitados, key=lambda v: dist[v])
    visitados.append(u)

    for v, w in grafo[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            previo[v] = u

Distancia_más_corta= [
    dist[i] if dist[i] != float('inf') else 1000000000
    for i in range(2, V + 1)
]
camino = []
actual = T
while actual is not None:
    camino.append(actual)
    actual = previo[actual]

camino.reverse()
print(*Distancia_más_corta)
print(*camino)
