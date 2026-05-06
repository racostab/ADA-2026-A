print("Dame el Grafo G(V,E)")
V, E = map(int, input().split())

# Inicializamos cada vértice con una lista vacía
grafo = {v: [] for v in range(1, V + 1)}

for _ in range(E):
    u, v = map(int, input().split())
    grafo[u].append(v)
    grafo[v].append(u)

#print(grafo)


def BFS(NI,grafo,visitado):
    cola = [NI]
    componente = []
    visitado.add(NI)
    
    while cola:
        u = cola.pop(0)
        componente.append(u)
        if u not in grafo:
            continue
        for v in grafo[u]:
            if v not in visitado:
                visitado.add(v)
                cola.append(v)
    return componente

def Conteo_Componentes(grafo):
    visitado = set()
    conteo = 0
    for nodo in grafo:
        if nodo not in visitado and nodo in grafo:
            BFS(nodo,grafo,visitado)
            conteo += 1
    return conteo

CompOriginal = Conteo_Componentes(grafo)
vertices_corte = []

for nodo in range(1,V+1):
    grafo_copia = {}
    for k in grafo:
        if k != nodo:
            nuevos_vecinos = []
            for x in grafo[k]:
                if x!=nodo:
                    nuevos_vecinos.append(x)
            grafo_copia[k] = nuevos_vecinos  
    comp = Conteo_Componentes(grafo_copia)
    #print("#################")
    #print(nodo,comp)
    if comp > CompOriginal:
        vertices_corte.append(nodo)

vertices_corte.sort()
#print("Vertices de Corte: ", vertices_corte)
print(*vertices_corte)