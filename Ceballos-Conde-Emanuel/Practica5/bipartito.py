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

rojo = []
azul = []
flag = 0

for v_inicial in vertices:
    if v_inicial not in rojo and v_inicial not in azul:
        rojo.append(v_inicial)
        cola = [v_inicial]
        
        while cola:
            actual = cola.pop(0)
            
            for vecino in grafo[actual]:
                if vecino not in rojo and vecino not in azul:
                    if actual in rojo:
                        azul.append(vecino)
                    else:
                        rojo.append(vecino)
                    cola.append(vecino)
                else:
                    if actual in rojo and vecino in rojo:
                        flag = 1
                    if actual in azul and vecino in azul:
                        flag = 1

if flag == 0:
    print(*sorted(set(rojo)))
    print(*sorted(set(azul)))
else:
    print()