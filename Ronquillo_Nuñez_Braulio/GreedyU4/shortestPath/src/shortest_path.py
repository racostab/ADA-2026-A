# Author: Ronquillo Nunez Braulio
# Shortest Path Problem

import heapq
import sys

INF = 1000000000


def dijkstra(vertices, graph):
    distances = [10**18] * (vertices + 1)
    parent = [0] * (vertices + 1)
    distances[1] = 0
    priority_queue = [(0, 1)]

    while priority_queue:
        current_distance, vertex = heapq.heappop(priority_queue)

        if current_distance != distances[vertex]:
            continue

        for neighbor, weight in graph[vertex]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parent[neighbor] = vertex
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, parent


def build_path(parent, distances, target):
    if target is None or target <= 0 or target >= len(distances):
        return []

    if distances[target] == 10**18:
        return []

    path = []
    current = target

    while current != 0:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))

    if not data:
        return

    vertices = data[0]
    edge_count = data[1]
    has_target = len(data) >= 3 + 3 * edge_count
    target = data[2] if has_target else None
    index = 3 if has_target else 2

    graph = [[] for _ in range(vertices + 1)]

    for _ in range(edge_count):
        if index + 2 >= len(data):
            return

        start = data[index]
        end = data[index + 1]
        weight = data[index + 2]
        index += 3

        if 1 <= start <= vertices and 1 <= end <= vertices:
            graph[start].append((end, weight))

    distances, parent = dijkstra(vertices, graph)

    output = []
    distance_line = []
    for vertex in range(2, vertices + 1):
        if distances[vertex] == 10**18:
            distance_line.append(str(INF))
        else:
            distance_line.append(str(distances[vertex]))

    output.append(" ".join(distance_line))

    if target is not None:
        output.append(" ".join(map(str, build_path(parent, distances, target))))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
