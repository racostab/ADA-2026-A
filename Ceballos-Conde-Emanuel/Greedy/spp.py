user_input = input()
graph_values = user_input.split() 
num_vertices = int(graph_values[0])
num_aristas = int(graph_values[1])
target = int(graph_values[2]) 

grafo_aristas = [[] for _ in range(num_vertices)]
vertices = [x + 1 for x in range(num_vertices)]

for i in range(num_aristas):
    u, v, w = map(int, input().split())
    grafo_aristas[u - 1].append([v, w])
    grafo_aristas[v - 1].append([u, w])

origen = 1 

valores_vertices = {v: [10**9, None] for v in vertices}
valores_vertices[origen][0] = 0

cola = list(vertices)

while len(cola) > 0:
    vertice_trabajo = min(cola, key=lambda k: valores_vertices[k][0])
    
    if valores_vertices[vertice_trabajo][0] == 10**9:
        break
        
    cola.remove(vertice_trabajo)

    for vecino_info in grafo_aristas[vertice_trabajo - 1]:
        vecino = vecino_info[0]
        peso = vecino_info[1]
        
        distancia_acumulada = valores_vertices[vertice_trabajo][0] + peso
        
        if distancia_acumulada < valores_vertices[vecino][0]:
            valores_vertices[vecino][0] = distancia_acumulada
            valores_vertices[vecino][1] = vertice_trabajo


distancias_output = []
for i in range(2, num_vertices + 1):
    distancias_output.append(str(valores_vertices[i][0]))

print(" ".join(distancias_output))

ruta = []
actual = target
while actual is not None:
    ruta.append(str(actual))
    actual = valores_vertices[actual][1]

    print(" ".join(ruta[::-1]))