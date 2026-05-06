def dfs(nodo, grafo, visitados, component):
    visitados[nodo] = True
    component.append(nodo)
    
    for vecino in grafo[nodo]:
        if not visitados[vecino]:
            dfs(vecino, grafo, visitados, component)

V, E = map(int, input().split())

grafo = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v = map(int, input().split())
    grafo[u].append(v)
    grafo[v].append(u)  

for i in range(1, V + 1):
    grafo[i].sort()

visited = [False] * (V + 1)
components = []

for i in range(1, V + 1):
    if not visited[i]:
        componente = []
        dfs(i, grafo, visited, componente)
        componente.sort()
        components.append(componente)

components.sort(key=lambda x: x[0])

print(len(components))
for comp in components:
    print(*comp)