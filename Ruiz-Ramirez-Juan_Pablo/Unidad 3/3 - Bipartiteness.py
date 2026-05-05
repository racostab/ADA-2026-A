V, E = map(int, input().split())
grafo = {v: [] for v in range(1, V + 1)}
for _ in range(E):
    u, v = map(int, input().split())
    grafo[u].append(v)
    grafo[v].append(u)

def BFS_bipartita(grafo):
    colores = {}
    for nodo in grafo:
        if nodo not in colores:
            cola = [nodo]
            colores[nodo] = 0
            while cola:
                R = cola.pop(0)
                for v in grafo[R]:
                    if v not in colores:
                        colores[v] = 1 - colores[R]
                        cola.append(v)
                    elif colores[v] == colores[R]:
                        return False, None
    return True, colores

Bipartita, colores = BFS_bipartita(grafo)
if Bipartita:
    U = sorted([n for n, c in colores.items() if c == 0])
    V = sorted([n for n, c in colores.items() if c == 1])
    print(*U)
    print(*V)
else:
    print("EMPTY")