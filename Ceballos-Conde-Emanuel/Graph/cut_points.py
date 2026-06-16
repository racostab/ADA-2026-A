user_input = input()
graph_values = user_input.split() 
num_vertices = int(graph_values[0])
num_aristas = int(graph_values[1])

grafo_aristas = [[] for _ in range(num_vertices)]
vertices = [x + 1 for x in range(num_vertices)]

for i in range(num_aristas):
    u, v = map(int, input().split())
    grafo_aristas[u - 1].append(v)
    grafo_aristas[v - 1].append(u)

grafo = dict(zip(vertices, grafo_aristas))

def puntos_de_corte(grafo):
    visitados = set()
    discovery = {}
    low = {}
    puntos = set()
    tiempo = [0]  # Se usa una lista para que sea mutable dentro de dfs

    def dfs(nodo, padre=-1):
        visitados.add(nodo)
        discovery[nodo] = low[nodo] = tiempo[0]
        tiempo[0] += 1
        hijos = 0
        
        for vecino in grafo.get(nodo, []):
            if vecino == padre:
                continue
            
            if vecino in visitados:
                low[nodo] = min(low[nodo], discovery[vecino])
            else:
                hijos += 1
                dfs(vecino, nodo)
                low[nodo] = min(low[nodo], low[vecino])
                
                if padre != -1 and low[vecino] >= discovery[nodo]:
                    puntos.add(nodo)
        
        if padre == -1 and hijos > 1:
            puntos.add(nodo)

    for nodo in grafo:
        if nodo not in visitados:
            dfs(nodo)
            
    return sorted(list(puntos))

resultado = puntos_de_corte(grafo)

print(*resultado)