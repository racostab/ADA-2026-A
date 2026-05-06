from collections import deque
import sys


def solve(data: str) -> str:
    if not data.strip():
        return ""

    values = list(map(int, data.split()))
    iterator = iter(values)
    vertices = next(iterator)
    edges = next(iterator)

    adjacency = [[] for _ in range(vertices + 1)]
    for _ in range(edges):
        left = next(iterator)
        right = next(iterator)
        adjacency[left].append(right)
        adjacency[right].append(left)

    color = [-1] * (vertices + 1)
    groups = [[], []]

    for start in range(1, vertices + 1):
        if color[start] != -1:
            continue

        color[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()
            groups[color[node]].append(node)

            for neighbor in adjacency[node]:
                if color[neighbor] == -1:
                    color[neighbor] = color[node] ^ 1
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return "EMPTY"

    groups[0].sort()
    groups[1].sort()
    if groups[0] and groups[1] and groups[0][0] > groups[1][0]:
        groups.reverse()

    return "\n".join(" ".join(map(str, group)) for group in groups)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
