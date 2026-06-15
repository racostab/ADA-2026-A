import sys


def solve(data):
    if not data.strip():
        return ''

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

    for node in range(1, vertices + 1):
        adjacency[node].sort()

    visited = [False] * (vertices + 1)
    components = []

    for start in range(1, vertices + 1):
        if visited[start]:
            continue

        stack = [start]
        visited[start] = True
        component = []

        while stack:
            node = stack.pop()
            component.append(node)

            for neighbor in reversed(adjacency[node]):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        component.sort()
        components.append(component)

    output = [str(len(components))]
    for component in components:
        output.append(' '.join(map(str, component)))

    return '\n'.join(output)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
