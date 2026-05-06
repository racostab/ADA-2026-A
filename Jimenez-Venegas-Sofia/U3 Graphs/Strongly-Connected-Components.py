from collections import defaultdict

def conected_c(V, edges):
    grafo = defaultdict(list)
    rev_grafo = defaultdict(list)
    for u, v in edges:
        grafo[u].append(v)
        rev_grafo[v].append(u)

    visitados = [False] * (V + 1)
    stack = []

    def dfs1(u):
        visitados[u] = True
        for v in grafo[u]:
            if not visitados[v]:
                dfs1(v)
        stack.append(u)

    for i in range(1, V + 1):
        if not visitados[i]:
            dfs1(i)

    visitados = [False] * (V + 1)
    sccs = []

    def dfs2(u, comp):
        visitados[u] = True
        comp.append(u)
        for v in rev_grafo[u]:
            if not visitados[v]:
                dfs2(v, comp)

    while stack:
        node = stack.pop()
        if not visitados[node]:
            comp = []
            dfs2(node, comp)
            comp.sort()
            sccs.append(comp)

    sccs.sort(key=lambda x: x[0])
    return sccs

V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

sccs = conected_c(V, edges)

print(len(sccs))
for comp in sccs:
    print(*comp)