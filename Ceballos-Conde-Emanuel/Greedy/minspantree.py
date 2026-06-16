import heapq

user_input = input()
graph_values = user_input.split() 
num_vertices = int(graph_values[0])
num_aristas = int(graph_values[1])
tipo_sp = graph_values[2]

grafo_aristas = [[] for _ in range(num_vertices)]
vertices = [x + 1 for x in range(num_vertices)]

for i in range(num_aristas):
    u, v, w = map(int, input().split())
    grafo_aristas[u - 1].append([v, w])
    grafo_aristas[v - 1].append([u, w])

def min_spanning_tree(num_vertices, grafo_aristas):
    cola_prioridad = [(0, 1)]
    visitados = [False] * (num_vertices + 1)
    costo_total = 0#
    mst_aristas = []

    while cola_prioridad:
        peso, u = heapq.heappop(cola_prioridad)

        if visitados[u]:
            continue
        
        visitados[u] = True
        costo_total += peso
        
        for v, w in grafo_aristas[u - 1]:
            if not visitados[v]:
                heapq.heappush(cola_prioridad, (w, v))
    
    return costo_total

def max_spanning_tree(num_vertices, grafo_aristas):
    cola_prioridad = [(-float('inf'), 1)]
    cola_prioridad = [(0, 1)] 
    
    visitados = [False] * (num_vertices + 1)
    costo_total = 0

    while cola_prioridad:
        peso_negativo, u = heapq.heappop(cola_prioridad)
        peso_real = -peso_negativo 

        if visitados[u]:
            continue
        
        visitados[u] = True
        costo_total += peso_real
        
        for v, w in grafo_aristas[u - 1]:
            if not visitados[v]:
                heapq.heappush(cola_prioridad, (-w, v))
    
    return costo_total

if tipo_sp == "min":
    print(f"{min_spanning_tree(num_vertices,grafo_aristas)}")
elif tipo_sp == "max":
    print(f"{max_spanning_tree(num_vertices,grafo_aristas)}")
