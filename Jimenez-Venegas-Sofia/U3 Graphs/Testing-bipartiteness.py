def bipartito(V, E):
    grafo = {i: [] for i in range(1, V + 1)}
    for u, v in E:
        grafo[u].append(v)
        grafo[v].append(u)

    color = [-1] * (V + 1)

    cola = [1]
    color[1] = 0
    front = 0 

    while front < len(cola):
        node = cola[front]
        front += 1

        for vecino in grafo[node]:
            if color[vecino] == -1:
                color[vecino] = 1 - color[node]
                cola.append(vecino)
            elif color[vecino] == color[node]:
                return None  

    U = [i for i in range(1, V + 1) if color[i] == 0]
    V_set = [i for i in range(1, V + 1) if color[i] == 1]

    return U, V_set

V, E = map(int, input().split())
edges = []
for _ in range(E):
    u, v = map(int, input().split())
    edges.append((u, v))

result = bipartito(V, edges)

if result is None:
    print("EMPTY")
else:
    U, V_set = result
    print(*sorted(U))
    print(*sorted(V_set))