# Given a graph G(V, E) where V is the number of vertices and E is the number of edges. A spanning tree ST of the graph G is a tree that spans G 
# (that is, it includes every vertex of G) and is a subgraph of G (every edge in the tree belongs to G). The weight of a spanning tree is the sum 
# of the weights of the edges in that tree. A minimum or maximum spanning tree is a spanning tree whose weight is less or more than (possibly equal) 
# to the weight of every other spanning tree.
 

# Given an undirected, weighted and connected graph G, find the weigth of a spanning tree.
# Input
# The input file contains one test case as described below. First line contains two space separated integers V (1 ≤ V ≤ 100, the number of vertices in t
# he graph) and E (1 ≤ E ≤ 100, the number of edges in the graph), and then three letter that specifies the tye of ST: min for minimum or max for maximum. 
# This is followed by E lines with three space-separated integers vi and vj (1 ≤ vi , vj ≤ 100) that specifies and edge between the vertex vi and vj, 
# and w that specifies the weight of the edge between the vertices.
# Output
# Output one integer denoting the total weight of the minimum or maximum spanning tree.
# Sample Input
# 6 9 min
# 1 2 2
# 2 3 3
# 3 4 5
# 4 5 9
# 5 1 4
# 2 6 7
# 3 6 8
# 1 4 1
# 2 4 3
# Sample Output
# 17

import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    xr, yr = find(parent, x), find(parent, y)
    if xr == yr:
        return False
    if rank[xr] < rank[yr]:
        parent[xr] = yr
    elif rank[xr] > rank[yr]:
        parent[yr] = xr
    else:
        parent[yr] = xr
        rank[xr] += 1
    return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    V = int(next(it))
    E = int(next(it))
    typ = next(it)  # "min" or "max"
    edges = []
    for _ in range(E):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u, v))

    # Sort edges: ascending for min, descending for max
    if typ == "min":
        edges.sort(key=lambda x: x[0])
    else:  # max
        edges.sort(key=lambda x: x[0], reverse=True)

    parent = [i for i in range(V + 1)]  # vertices are 1-indexed
    rank = [0] * (V + 1)

    total_weight = 0
    edges_used = 0
    for w, u, v in edges:
        if union(parent, rank, u, v):
            total_weight += w
            edges_used += 1
            if edges_used == V - 1:
                break

    print(total_weight)

if __name__ == "__main__":
    main()