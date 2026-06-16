# Given a graph G(V, E) where V is the number of vertices and E is the number of edges. A connected component or simply component of an 
# undirected graph G is a subgraph in which each pair of nodes is connected with each other via a path. The main point here is reachability.

# Given an undirected graph, print all connected components line by line.
# Input
# The input file contains one test case as described below. First line contains two space separated integers V (1 ≤ V ≤ 100) and 
# E (1 ≤ E ≤ 100). This is followed by E lines with two integers vi and vj (1 ≤ vi , vj ≤ 100) that specifies an edge between the 
# vertex vi and vj.
# Output
# First line contains one integer CC (1 ≤ CC ≤ 100) specifying the number of connected component. This is followed by CC lines, t
# he list of vertex of a connected component, on a line by itself, each vertex is arranged from lowest to highest value -sorted 
# ascending (considering 1-indexed arrays). The lists are printed using the index of the first vertex.
# Sample Input
# 12 11
# 1 4
# 4 5
# 1 2
# 1 3
# 2 3
# 3 5
# 3 6
# 7 9
# 7 8
# 11 10
# 10 12
# Sample Output
# 3
# 1 2 3 4 5 6
# 7 8 9
# 10 11 12
from collections import deque

def entrada():
    V,E = map(int, input().split())
    edges = []
    for _ in range(E):
        vi , vj = map(int, input().split())
        edges.append([vi, vj])

    return V, edges

def build_grap(V, edges):
    grap = {i: [] for i in range(1, V + 1)}
    for vi, vj in edges:
        grap[vi].append(vj)
        grap[vj].append(vi)  # grafo no dirigido: arista en ambos sentidos
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

def print_output(c):
    print(len(c))
    for i in c:
        print(*i)

def main():
    V,edges = entrada()
    grap = build_grap(V, edges)
    #s = 1  # vértice de partida (no confundir E = cantidad de aristas)
    componentes = components(grap)
    print_output(componentes)

if __name__ == "__main__":
    main()