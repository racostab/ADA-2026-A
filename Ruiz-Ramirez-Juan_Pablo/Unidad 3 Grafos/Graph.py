print("Dame el Grafo G(V,E)")
V, E = map(int, input().split())

# Inicializamos cada vértice con una lista vacía
grafo = {v: [] for v in range(1, V + 1)}

for _ in range(E):
    u, v = map(int, input().split())
    grafo[u].append(v)
    grafo[v].append(u)

visitado = set()

def BFS(NI,grafo,visitado):
    cola = [NI]
    componente = []
    visitado.add(NI)
    
    while cola:
        u = cola.pop(0)
        componente.append(u)
        for v in grafo[u]:
            if v not in visitado:
                visitado.add(v)
                cola.append(v)
    return componente

componentes = []
for nodo in range(1,V+1):
    if nodo not in visitado:
        comp=BFS(nodo,grafo,visitado)
        comp.sort()
        componentes.append(comp)

print(len(componentes))
for comp in componentes:
    print(*comp)
