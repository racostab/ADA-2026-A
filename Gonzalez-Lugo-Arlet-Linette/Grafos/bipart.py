# Author: Gonzalez Arlet
from collections import deque

def es_bipartito(vertices, aristas):
    adj = [[] for _ in range(vertices + 1)]
    for u, v in aristas:
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (vertices + 1)
    
    for inicio in range(1, vertices + 1):
        if color[inicio] == 0:
            color[inicio] = 1
            cola = deque([inicio])
            
            while cola:
                u = cola.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        cola.append(v)
                    elif color[v] == color[u]:
                        return False, None, None
    
    U = [i for i in range(1, vertices + 1) if color[i] == 1]
    V = [i for i in range(1, vertices + 1) if color[i] == -1]
    return True, U, V

V, E = map(int, input().split())
aristas = []
for i in range(E):
    u, v = map(int, input().split())
    aristas.append((u, v))

bipartito, U, V_set = es_bipartito(V, aristas)

if not bipartito:
    print("EMPTY")
else:
    print(" ".join(map(str, U)))
    print(" ".join(map(str, V_set)))