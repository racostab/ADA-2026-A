import sys

sys.setrecursionlimit(2000)

def obtener_componentes(num_vertices, aristas):
    adj = [[] for _ in range(num_vertices + 1)]
    rev_adj = [[] for _ in range(num_vertices + 1)]
    for u, v in aristas:
        adj[u].append(v)
        rev_adj[v].append(u)

    visitado = [False] * (num_vertices + 1)
    orden = []

    def dfs1(u):
        visitado[u] = True
        for v in adj[u]:
            if not visitado[v]:
                dfs1(v)
        orden.append(u)

    for i in range(1, num_vertices + 1):
        if not visitado[i]:
            dfs1(i)

    visitado = [False] * (num_vertices + 1)
    componentes = []

    def dfs2(u, comp):
        visitado[u] = True
        comp.append(u)
        for v in rev_adj[u]:
            if not visitado[v]:
                dfs2(v, comp)

    for i in reversed(orden):
        if not visitado[i]:
            comp = []
            dfs2(i, comp)
            comp.sort()
            componentes.append(comp)

    componentes.sort(key=lambda x: x[0])
    return componentes

def resolver():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    num_vertices = int(entrada[0])
    num_aristas = int(entrada[1])
    
    aristas = []
    idx = 2
    for _ in range(num_aristas):
        u = int(entrada[idx])
        v = int(entrada[idx + 1])
        aristas.append((u, v))
        idx += 2

    resultado = obtener_componentes(num_vertices, aristas)

    print(len(resultado))
    for comp in resultado:
        print(" ".join(map(str, comp)))

resolver()