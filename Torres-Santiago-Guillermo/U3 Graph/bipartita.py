def dfs_(u):    
    if visitados[u-1] == 1:
        return True
    
    visitados[u-1] = 1

    if u not in verde and u not in rojo: 
        verde.append(u)

    for v in grafo[u]:
        
        if (u in verde and v in verde) or (u in rojo and v in rojo):
            return False

        if visitados[v-1] == 0:
            if u in verde:
                rojo.append(v)
            else:
                verde.append(v)
            
            if not dfs_(v):
                return False
        
    verde.sort()
    rojo.sort()
    return True

def print_rojo():
    for c in range(l_r):
        if c == l_r-1:
            print(f"{rojo[c]}")
        else:
            print(f"{rojo[c]}", end=" ")

def print_verde():
    for c in range(l_v):
        if c == l_v-1:
            print(f"{verde[c]}")
        else:
            print(f"{verde[c]}", end=" ")
            
datos_g = input().split()

nodos = int(datos_g[0])
aristas = int(datos_g[1])

grafo = {}
for k in range(1,nodos+1):
    grafo.update({k:[]})

for k1 in range(aristas):
    pareja = input().split()    
    grafo[int(pareja[0])].append(int(pareja[1]))
    grafo[int(pareja[1])].append(int(pareja[0]))

visitados = [0]*nodos
componentes = []

verde = []
rojo = []
bipartita = True

for nodo in grafo.keys():
    if visitados[nodo-1] == 0:
        if not dfs_(nodo):
            bipartita = False
if bipartita:
    l_v = len(verde)
    l_r = len(rojo)

    if l_v <= l_r:
        print_verde()
        print_rojo()
    else:
        print_rojo()
        print_verde()
else:
    print("EMPTY")
