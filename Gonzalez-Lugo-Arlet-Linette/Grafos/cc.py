#Gonzalez Arlet CC

entrada = input().split()
V = int(entrada[0])
E = int(entrada[1])

# Crear grafo
grafo = {i: [] for i in range(1, V + 1)}

def dfs(nodo, grafo, visitado, comp):
    visitado[nodo] = True
    comp.append(nodo)
    
    for vecino in grafo[nodo]:
        if not visitado[vecino]:
            dfs(vecino, grafo, visitado, comp)

for _ in range(E):
    datos = input().split()
    u = int(datos[0])
    v = int(datos[1])
    
    grafo[u].append(v)
    grafo[v].append(u)

# Ordenar vecinos
for nodo in grafo:
    grafo[nodo].sort()

visitado = {i: False for i in range(1, V + 1)}
componentes = []

for nodo in range(1, V + 1):
    if not visitado[nodo]:
        comp = []
        dfs(nodo, grafo, visitado, comp)
        componentes.append(sorted(comp))
componentes.sort(key=lambda x: x[0])

print(len(componentes))
for comp in componentes:
    print(*comp)