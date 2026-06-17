import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # Path compression
    return parent[x]

def union(parent, rank, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry:
        return False
    # Union by rank
    if rank[rx] < rank[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    if rank[rx] == rank[ry]:
        rank[rx] += 1
    return True

def kruskal(V, edges, maximize=False):
    # Sort edges by weight (descending if maximize, ascending if minimize)
    edges.sort(key=lambda e: e[2], reverse=maximize)

    parent = list(range(V + 1))
    rank = [0] * (V + 1)

    total_weight = 0
    edges_used = 0

    for u, v, w in edges:
        if union(parent, rank, u, v):
            total_weight += w
            edges_used += 1
            if edges_used == V - 1:
                break

    return total_weight

def main():
    data = sys.stdin.read().split()
    idx = 0

    V = int(data[idx]); idx += 1
    E = int(data[idx]); idx += 1
    st_type = data[idx];  idx += 1  # "min" or "max"

    edges = []
    for _ in range(E):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))

    maximize = (st_type == "max")
    result = kruskal(V, edges, maximize)
    print(result)

if __name__ == "__main__":
    main()