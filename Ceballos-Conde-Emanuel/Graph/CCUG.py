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

def comp_conex(grafo):
    visitados = set()
    componentes = []

    def dfs(nodo, componente_actual):
        visitados.add(nodo)
        componente_actual.append(nodo)
        
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                dfs(vecino, componente_actual)

    for nodo in grafo:
        if nodo not in visitados:
            nueva_componente = []
            dfs(nodo, nueva_componente)
            componentes.append(nueva_componente)
            
    return componentes

resultado = comp_conex(grafo)

print(len(resultado))
for subgrafo in resultado:
    subgrafo.sort()
    print(*subgrafo)