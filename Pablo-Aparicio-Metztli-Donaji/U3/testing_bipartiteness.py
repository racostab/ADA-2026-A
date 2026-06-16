# A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V such that every edge (u, v) either connects a vertex from U to V or a vertex from V to U. 
# In other words, for every edge (u, v), either u belongs to U and v to V, or u belongs to V and v to U. We can also say that there is no edge that connects vertices of same set.

# Figure 1.- Example of a bipartite graph.

# Given a connected graph G, find the two independent sets U and V.
# Input
# The input file contains one test case as described below. First line contains two space separated integers V (1 ≤ V ≤ 100, the number of vertices in the graph) and E (1 ≤ E ≤ 100, 
# the number of edges in the graph).
# Output
# Output two list of integers denoting the vertices of set U and V, on a line by itself. Each list is arranged from lowest to highest value (sorted ascending) and the lists are printed 
# using the index of the first vertex.
# If the graph is not a bipartite graph, print one line with the string EMPTY.
# Sample Input
# 7 11
# 1 2
# 1 4
# 1 5
# 1 7
# 2 3
# 2 6
# 3 4
# 3 5
# 3 7
# 5 6
# 6 7
# Sample Output
# 1 3 6
# 2 4 5 7
from collections import deque

def entrada():
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        vi, vj = map(int, input().split())
        edges.append([vi, vj])

    return V, edges

def build_grap(V, edges):
    grap = {i: [] for i in range(1, V + 1)}
    for vi, vj in edges:
        grap[vi].append(vj)
        grap[vj].append(vi)
    return grap

def bfs_bipartite(grap, s, color):
    color[s] = 0
    queue = deque([s])

    while queue:
        u = queue.popleft()
        for v in grap[u]:
            if v not in color:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                return False

    return True

def bipartite_sets(V, grap):
    color = {}

    for s in range(1, V + 1):
        if s not in color:
            if not bfs_bipartite(grap, s, color):
                return None

    U = sorted(v for v in range(1, V + 1) if color[v] == 0)
    W = sorted(v for v in range(1, V + 1) if color[v] == 1)

    if U[0] > W[0]:
        U, W = W, U

    return U, W

def print_output(result):
    if result is None:
        print("EMPTY")
    else:
        U, W = result
        print(*U)
        print(*W)

def main():
    V, edges = entrada()
    grap = build_grap(V, edges)
    result = bipartite_sets(V, grap)
    print_output(result)

if __name__ == "__main__":
    main()