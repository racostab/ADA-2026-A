# A vertex in an undirected connected graph is a cut vertex (or an articulation point) if removing it (and edges through it) disconnects the graph. 
# Cut vertex represent vulnerabilities in a connected network – single points whose failure would split the network into 2 or more components. 
# They are useful for designing reliable networks. For a disconnected undirected graph, a cut vertex is a vertex removing which increases number of 
# connected components. Given an undirected G(V, E) where V is the number of vertices and E is the number of edges, find the cut-points in the graph G.

 
# Figure 1.- Example of cut points in a Graph.

# Given an undirected G(V, E) where V is the number of vertices and E is the number of edges, find the cut-points in the graph G.
# Input
# The input file contains one test case as described below. First line contains two space separated integers V (1 ≤ V ≤ 100) and E (1 ≤ E ≤ 100). This is 
# followed by E lines with two integers vi and vj (1 ≤ vi , vj ≤ 100) that specifies and edge between the vertex vi and vj.
# Output
# Output the list of cut-points (integers denoting the vertices) arranged from lowest to highest value -sorted ascending.
# Sample Input
# 5 5
# 1 2
# 1 4
# 4 2
# 2 3
# 3 5
# Sample Output
# 2 3
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

def dfs(u, parent, grap, visited, disc, low, time, articulation):
    visited.add(u)
    time[0] += 1
    disc[u] = low[u] = time[0]
    children = 0

    for neighbor in grap[u]:
        if neighbor not in visited:
            children += 1
            dfs(neighbor, u, grap, visited, disc, low, time, articulation)
            low[u] = min(low[u], low[neighbor])
            if parent == -1 and children > 1:
                articulation.add(u)
            if parent != -1 and low[neighbor] >= disc[u]:
                articulation.add(u)
        elif neighbor != parent:
            low[u] = min(low[u], disc[neighbor])

def find_cut_points(V, grap):
    visited = set()
    disc = {}
    low = {}
    time = [0]
    articulation = set()

    for s in range(1, V + 1):
        if s not in visited:
            dfs(s, -1, grap, visited, disc, low, time, articulation)

    return sorted(articulation)

def print_output(cut_points):
    print(*cut_points)

def main():
    V, edges = entrada()
    grap = build_grap(V, edges)
    cut_points = find_cut_points(V, grap)
    print_output(cut_points)

if __name__ == "__main__":
    main()
