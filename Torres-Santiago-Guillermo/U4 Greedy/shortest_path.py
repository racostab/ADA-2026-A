def shortest_path(V, A):
    dist = [1000000000] * (V+1)
    dist[1] = 0
    camino = [[1] for i in range(V + 1)]
    

    for i in range(V):
        
        for a in A:
            u, v, w = a
            if dist[u] != 1000000000 and dist[u] + w < dist[v]:
                if i == V-1:
                    return [-1]
                
                dist[v] = dist[u] + w
                
                camino[v] = camino[u] + [v]

    return dist,camino[1:]

"""
nodos = 5
aristas = [[1, 2, 5], [1, 3, 2], [3, 4, 1], [1, 4, 6], [3, 5, 5]]
target = 4
#"""

datos_g = input().split()
if len(datos_g) == 3:
    nodos = int(datos_g[0])
    n_aristas = int(datos_g[1])
    target = int(datos_g[2])
else:
    nodos = int(datos_g[0])
    n_aristas = int(datos_g[1])
    target = None

aristas = []
for k in range(n_aristas):
    aristas.append(list(map(int,input().split())))

short_dist,camino = shortest_path(nodos, aristas)

for k1 in range(2,nodos+1):   
    if k1 == nodos:
        print(f"{short_dist[k1]}")
    else:
        print(f"{short_dist[k1]}", end=" ")

#"""
if target != None:
    n_cam = len(camino[target-1])

    for k2 in range(n_cam):   
        if k2 == n_cam-1:
            print(f"{camino[target-1][k2]}")
        else:
            print(f"{camino[target-1][k2]}", end=" ")
#"""
