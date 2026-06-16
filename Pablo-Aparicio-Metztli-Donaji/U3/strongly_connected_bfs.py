# Connectivity in an undirected graph means that every vertex can reach every other vertex via any path. If the graph is not connected the graph can 
# be broken down into Connected Components. Strong Connectivity applies only to directed graphs. A directed graph is strongly connected if there is a 
# directed path from any vertex to every other vertex. This is same as connectivity in an undirected graph, the only difference being strong connectivity 
# applies to directed graphs and there should be directed paths instead of just paths. Similar to connected components, a directed graph can be broken 
# down into Strongly Connected Components.

# Given an directed graph, print all connected components line by line.
# Input
# The input file contains one test case as described below. First line contains two space separated integers V (1 ≤ V ≤ 100) and E (1 ≤ E ≤ 100). This is 
# followed by E lines with two integers vi and vj (1 ≤ vi , vj ≤ 100) that specifies a directed edge (often called arc) between the vertex vi and vj.
# Output
# First line contains one integer CC (1 ≤ CC ≤ 100) specifying the number of connected component. This is followed by CC lines, the list of vertex of a 
# connected component, on a line by itself, each vertex is arranged from lowest to highest value -sorted ascending (considering 1-indexed arrays). 
# The lists are printed using the index of the first vertex.
# Sample Input
# 12 20
# 1 2
# 2 3
# 2 4
# 2 5
# 5 2
# 4 5
# 3 6
# 6 3
# 5 6
# 7 8
# 8 7
# 7 10
# 9 7
# 10 9
# 10 11
# 11 12
# 12 10
# 4 7
# 5 7
# 6 8
# Sample Output
# 4
# 1
# 2 4 5
# 3 6
# 7 8 9 10 11 12
from collections import deque

def entrada():
    V,E = map(int, input().split())
    edges = []
    for _ in range(E):
        vi , vj = map(int, input().split())
        edges.append([vi, vj])

    return V,E, edges

def build_grap(V, edges):
    grap = {i: [] for i in range(1, V+1)}
    for vi ,vj in edges:
        grap[vi].append(vj)
    return grap

def bfs(grap,s,R):
    # Marcamos s como visitado
    R.add(s)
    # Componente 
    c = []
    # Iniciamos con S, entra por la derecha
    queue = deque([s])
    # mientras la cola no este vacia entra al ciclo
    while queue:
        # asignamos el valor de la cola y lo sacamos por la izquierda
        u = queue.popleft()
        # Guardamos el componente 
        c.append(u)
        # visitamos los vecinos del nodo u
        for v in grap[u]:
            # si no esta el vecino en la cola entra al if
            if v not in R:
                # agregamos el nodo al conjunto y a la cola
                R.add(v)
                queue.append(v)
    return sorted(c)

def components(grap):
    # Set vacio para revizar si ya se visito un nodo
    R = set()
    # Componente
    c = []

    for nodo in sorted(grap.keys()):
        if nodo not in R:
            comp = bfs(grap,nodo,R)
            c.append(comp)
    
    c.sort(key=lambda cm: cm[0])
    return c


def main():
    # El grafo representado como un diccionario (Lista de adyacencia)
    #grap = {
    #    'A': ['B', 'C'],
    #    'B': ['A', 'D'],
    #    'C': ['A', 'D', 'E'],
    #    'D': ['B', 'C'],
    #    'E': ['C']
    #}

    # punto de partida (s)
    #s = 'A'

    V,E, edges = entrada()
    grap = build_grap(V, edges)
    #s = 1  # vértice de partida (no confundir E = cantidad de aristas)
    R = components(grap)
    print(R)

if __name__ == "__main__":
    main()