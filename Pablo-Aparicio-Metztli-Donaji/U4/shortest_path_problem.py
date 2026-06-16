# You are given 2 integers (N,M), N is the number of vertices, M is the number of edges. You'll also be given ai, bi, wi where ai and bi represents an edge from a vertex ai to a vertex bi and wi respresents the weight of that edge. Task is to find the shortest path from source vertex (vertex number 1) to all other vertices (vi) where (2 ≤ i ≤ N).
# Input
# First line contains two space separated integers, (N,M). Then M lines follow, each line has 3 space separated integers ai, bi, wi.
# Output
# Print the shortest distances from the source vertex (vertex number 1) to all other vertices (vi) where (2 ≤ i ≤ N). Print "109" in case the vertex "vi" can't be reached form the source vertex. Leave a space between any 2 printed numbers.

# Constraints:
# (1 ≤ N ≤ 104)
# (1 ≤ M ≤ 106)
# (1 ≤ i ≤ N)
# (1 ≤ i ≤ 1000)

# Sample Input
# 5 5 4
# 1 2 5
# 1 3 2
# 3 4 1
# 1 4 6
# 3 5 5
# Sample Output
# 5 2 3 7
# 1 3 4

from heapq import heappush, heappop

def entrada():
    datos = list(map(int, input().split()))
    v, e = datos[0], datos[1]
    destino = datos[2] if len(datos) > 2 else v
    g = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, w = map(int, input().split())
        g[a].append((b, w))

    return v, g, destino

def dijkstra(n, g, s):
    INF = float('inf')
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)

    dist[s] = 0
    pq = []
    heappush(pq, (0, s))

    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in g[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
                heappush(pq, (dist[v], v))

    return dist, parent


def reconstruct_path(parent, src, dst):
    path = []
    node = dst
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()
    if not path or path[0] != src:
        return []
    return path

def main():
    v, g, destino = entrada()
    src = 1
    dist, parent = dijkstra(v, g, src)

    for i in range(2, v + 1):
        print(109 if dist[i] == float('inf') else int(dist[i]))
    print()

    if dist[destino] == float('inf'):
        print(109)
    else:
        path = reconstruct_path(parent, src, destino)
        #print(*path)
        # print(int(dist[destino]))

if __name__ == "__main__":
    main()