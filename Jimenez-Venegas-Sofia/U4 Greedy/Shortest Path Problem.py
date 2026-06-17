import heapq
import sys

INF = 10**9

n, m, target = map(int, sys.stdin.readline().split())

grafo = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    grafo[a].append((b, w))

dist = [INF] * (n + 1)
padre = [-1] * (n + 1)

dist[1] = 0

pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)

    if d != dist[u]:
        continue

    for v, w in grafo[u]:
        nd = d + w

        if nd < dist[v]:
            dist[v] = nd
            padre[v] = u
            heapq.heappush(pq, (nd, v))

# Imprimir distancias de 2..N
print(*dist[2:])

if dist[target] == INF:
    print(-1)
else:
    path = []
    cur = target

    while cur != -1:
        path.append(cur)
        cur = padre[cur]

    path.reverse()
    print(*path)