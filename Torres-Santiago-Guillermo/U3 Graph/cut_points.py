"""
    Puntos de corte
    Grafos
    Algoritmo DFS Busqueda en profundida

    Centro de Investigacion en Computacion
    Analisis y Diseño de Algoritmos
    
    Torres Santiago Guillermo A260486
    Maestria en Ciencias en Ingenieria de Computo

    14/Marzo/2026 

"""
import copy

# ---------------------- Busqueda profunda ---------------------------
def dfs_(u,pila_r):    
    if visitados[u-1] == 1: # Si el nodo fue visitado, retrocede
        return
    
    visitados[u-1] = 1  # Marcar nodo como visitado
    if u not in pila_r: 
        pila_r.append(u)    # Agregar nodo a pila si no esta ya
    
    for v in grafo[u]:
        if visitados[v-1] == 0: # Agregar nodo si no se a visitado
            pila_r.append(v)
            dfs_(v,pila_r)
    pila_r.sort()

#---------------------- Calcular componentes conexas
def comp_conex():
    global visitados
    global componentes
    
    visitados = [0]*nodos   # Arreglo para marcar nodos no visitados
    componentes = []

    for nodo in grafo.keys():
        if visitados[nodo-1] == 0:      # Si el nodo no ha sido visitado
            pila_r = []                 # Inicializar pila de nodos visitados
            pila_r = dfs_(nodo,pila_r)  # Recorre grafo
            componentes.append(pila_r)  # 
    cc = len(componentes)   # Numero de componentes conexas
    return cc
    
#--------------------------- Puntos de corte ---------------------------
def puntos_corte():
    global grafo
    
    cc_i = comp_conex() # Calcular componentes conexas originales

    for n1 in grafo_o:
        grafo_corte = copy.deepcopy(grafo_o)
        del grafo_corte[n1]                 # Eliminar nodo
        for n2 in  grafo_corte:
            if n1 in grafo_corte[n2]:
                grafo_corte[n2].remove(n1)  # Eliminar las aristas
        #print(grafo_corte)
        
        grafo = copy.deepcopy(grafo_corte)
        cc_f = comp_conex() # Calular componentes conexas del nuevo grafo
        #print(cc_f)
        if cc_f > cc_i:         # Si hay mas componentes, el nodo es punto de corte
            puntos.append(n1)   

# ---------------------------- MAIN ---------------------------------

#""" Entrada de teclado
datos_g = input().split()

nodos = int(datos_g[0])
aristas = int(datos_g[1])

grafo_o = {}
for k in range(1,nodos+1):      # Inicializar lista con nodos
    grafo_o.update({k:[]})

for k1 in range(aristas):       # Agregar las aristas a la lista
    pareja = input().split()    
    grafo_o[int(pareja[0])].append(int(pareja[1]))    # Agregar en ambas direcciones
    grafo_o[int(pareja[1])].append(int(pareja[0]))    # Para grafos no direccionados
#"""


visitados = [0]*nodos   # Arreglo para marcar nodos no visitados
componentes = []
puntos = []             # Almacenar puntos de corte
grafo = copy.deepcopy(grafo_o)

puntos_corte()          # Obtener los puntos de corte

np = len(puntos)
for k2 in range(np):
    if k2 == np-1:
        print(f"{puntos[k2]}")    # Nodos que son puntos de corte
    else:
        print(f"{puntos[k2]}", end=" ")
