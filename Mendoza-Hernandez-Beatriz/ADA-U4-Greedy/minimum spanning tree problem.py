class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1

        return True


def kruskal(v, edges, mst_type):
    if mst_type == "min":
        edges.sort(key=lambda x: x[2])          # Ascendente
    else:
        edges.sort(key=lambda x: x[2], reverse=True)  # Descendente

    uf = UnionFind(v)
    total_weight = 0
    edges_used = 0

    for u, w, weight in edges:
        if uf.union(u, w):
            total_weight += weight
            edges_used += 1

            if edges_used == v - 1:
                break

    return total_weight


# Lectura de entrada
first_line = input().split()
V = int(first_line[0])
E = int(first_line[1])
mst_type = first_line[2]

edges = []

for _ in range(E):
    vi, vj, w = map(int, input().split())
    edges.append((vi, vj, w))

print(kruskal(V, edges, mst_type))