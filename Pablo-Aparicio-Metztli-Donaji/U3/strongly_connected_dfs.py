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
def entrada():
    V, E = map(int, input().split())
    edges = []
    edges_inv = []
    for _ in range(E):
        vi, vj = map(int, input().split())
        edges.append([vi, vj])
        edges_inv.append([vj, vi])

    return V, edges, edges_inv

def build_grap(V, edges):
    grap = {i: [] for i in range(1, V+1)}
    for vi ,vj in edges:
        grap[vi].append(vj)
    return grap

def dfs(s, grap, visited, orden):
    visited.add(s)
    for neighbor in grap[s]:
        if neighbor not in visited:
            dfs(neighbor, grap, visited, orden)
    orden.append(s)


def dfs_componente(s, grap_inv, visited, componente):
    visited.add(s)
    componente.append(s)
    for neighbor in grap_inv[s]:
        if neighbor not in visited:
            dfs_componente(neighbor, grap_inv, visited, componente)


def kosaraju(V, grap, grap_inv):
    visited = set()
    orden = []

    for s in range(1, V + 1):
        if s not in visited:
            dfs(s, grap, visited, orden)

    visited = set()
    componentes = []

    for s in reversed(orden):
        if s not in visited:
            componente = []
            dfs_componente(s, grap_inv, visited, componente)
            componentes.append(sorted(componente))

    componentes.sort(key=lambda c: c[0])
    return componentes

def print_output(c):
    print(len(c))
    for i in c:
        print(*i)

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

    V, edges, edges_inv = entrada()
    grap = build_grap(V, edges)
    grap_inv = build_grap(V, edges_inv)
    componentes = kosaraju(V, grap, grap_inv)
    print_output(componentes)

if __name__ == "__main__":
    main()