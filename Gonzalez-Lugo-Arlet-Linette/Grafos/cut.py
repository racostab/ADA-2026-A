def encontrar_puntos_articulacion(V, aristas):
    grafo = {i: [] for i in range(1, V + 1)}
    for u, v in aristas:
        grafo[u].append(v)
        grafo[v].append(u)

    visitado = [False] * (V + 1)
    descubrimiento = [-1] * (V + 1)
    mas_bajo = [-1] * (V + 1)
    padre = [-1] * (V + 1)
    puntos_articulacion = set()
    tiempo = 0

    def dfs(u):
        nonlocal tiempo
        hijos = 0
        visitado[u] = True
        descubrimiento[u] = mas_bajo[u] = tiempo
        tiempo += 1

        for v in grafo[u]:
            if not visitado[v]:
                padre[v] = u
                hijos += 1
                dfs(v)
                mas_bajo[u] = min(mas_bajo[u], mas_bajo[v])
                if padre[u] == -1 and hijos > 1:
                    puntos_articulacion.add(u)
                if padre[u] != -1 and mas_bajo[v] >= descubrimiento[u]:
                    puntos_articulacion.add(u)
            elif v != padre[u]:
                mas_bajo[u] = min(mas_bajo[u], descubrimiento[v])

    for i in range(1, V + 1):
        if not visitado[i]:
            dfs(i)

    return sorted(puntos_articulacion)


if __name__ == "__main__":
    V, E = map(int, input().split())
    
    aristas = []
    for i in range(E):
        u, v = map(int, input().split())
        aristas.append((u, v))
    
    resultado = encontrar_puntos_articulacion(V, aristas)
    
    if resultado:
        print(" ".join(map(str, resultado)))  
    else:
        print("")
