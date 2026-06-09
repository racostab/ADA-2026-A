"""
    Componentes conexas
    Grafos
    Algoritmo DFS Busqueda en profundida

    Centro de Investigacion en Computacion
    Analisis y Diseño de Algoritmos
    
    Torres Santiago Guillermo A260486
    Maestria en Ciencias en Ingenieria de Computo

    14/Marzo/2026 

"""
# ---------------------- Busqueda profunda ---------------------------
def dfs_(u):    
    if visitados[u-1] == 1: # Si el nodo fue visitado, retrocede
        return
    
    visitados[u-1] = 1  # Marcar nodo como visitado
    if u not in pila_r: 
        pila_r.append(u)    # Agregar nodo a pila si no esta ya
    
    for v in grafo[u]:
        if visitados[v-1] == 0: # Agregar nodo si no se a visitado
            pila_r.append(v)
            dfs_(v)
    pila_r.sort()

# ---------------------------- MAIN ---------------------------------

""" Caso de prueba
nodos = 12
aristas = 11
grafo = {1: [4, 2, 3], 2: [1, 3], 3: [1, 2, 5, 6], 4: [1, 5], 5: [4, 3], 6: [3], 7: [9, 8], 8: [7], 9: [7], 10: [11, 12], 11: [10], 12: [10]}
# Solucion:
# 3
# 1 2 3 4 5 6
# 7 8 9
# 10 11 12
#"""


#""" Entrada de teclado
datos_g = input().split()

nodos = int(datos_g[0])
aristas = int(datos_g[1])

grafo = {}
for k in range(1,nodos+1):      # Inicializar lista con nodos
    grafo.update({k:[]})

for k1 in range(aristas):       # Agregar las aristas a la lista
    pareja = input().split()    
    grafo[int(pareja[0])].append(int(pareja[1]))    # Agregar en ambas direcciones
    grafo[int(pareja[1])].append(int(pareja[0]))    # Para grafos no direccionados
#"""


visitados = [0]*nodos   # Arreglo para marcar nodos no visitados
componentes = []        

#for n in grafo:  
 #   print(f"{n}: {grafo[n]}")

for nodo in grafo.keys():
    if visitados[nodo-1] == 0:      # Si el nodo no ha sido visitado
        pila_r = []                 # Inicializar pila de nodos visitados
        dfs_(nodo)                  # Recorre grafo
        componentes.append(pila_r)  # 


cc = len(componentes)   # Numero de componentes conexas
print(cc)
#print(componentes)

for k2 in range(cc):
    sn = len(componentes[k2])
    for k3 in range(sn):   
        if k3 == sn-1:
            print(f"{componentes[k2][k3]}")    # Nodos que componen los componentes
        else:
            print(f"{componentes[k2][k3]}", end=" ")
