import sys
import heapq

def dijkstra(n, graph):
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[1] = 0

    pq = [(0, 1)]  # (distancia, nodo)

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n, m = data[0], data[1]

    graph = [[] for _ in range(n + 1)]

    idx = 2
    for _ in range(m):
        a, b, w = data[idx], data[idx + 1], data[idx + 2]
        graph[a].append((b, w))
        idx += 3

    dist = dijkstra(n, graph)

    result = []
    for i in range(2, n + 1):
        if dist[i] == 10**18:
            result.append("1000000000")
        else:
            result.append(str(dist[i]))

    print(" ".join(result))

if __name__ == "__main__":
    main()