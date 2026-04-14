#Author: Braulio Alberto Ronquillo Nunez
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

    discovery = [0] * (vertices + 1)
    low = [0] * (vertices + 1)
    is_cut = [False] * (vertices + 1)
    timer = 0

    sys.setrecursionlimit(max(1000, vertices + 10))

    def dfs(node: int, parent: int) -> None:
        nonlocal timer
        timer += 1
        discovery[node] = timer
        low[node] = timer
        children = 0

        for neighbor in adjacency[node]:
            if neighbor == parent:
                continue

            if discovery[neighbor] == 0:
                children += 1
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])

                if parent != 0 and low[neighbor] >= discovery[node]:
                    is_cut[node] = True
            else:
                low[node] = min(low[node], discovery[neighbor])

        if parent == 0 and children > 1:
            is_cut[node] = True

    for node in range(1, vertices + 1):
        if discovery[node] == 0:
            dfs(node, 0)

    return " ".join(str(node) for node in range(1, vertices + 1) if is_cut[node])


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
