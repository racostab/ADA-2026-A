# Author: Ronquillo Nunez Braulio
# Optional task: tree implemented with a table

import sys


def validate_tree(nodes, root):
    if root not in nodes:
        return False, "raiz inexistente"

    parent = {}

    for node_id, (_, left, right) in nodes.items():
        for child in (left, right):
            if child == -1:
                continue

            if child not in nodes:
                return False, f"hijo inexistente: {child}"

            if child in parent:
                return False, f"dos padres para nodo: {child}"

            parent[child] = node_id

    visited = set()
    visiting = set()

    def dfs(node_id):
        if node_id in visiting:
            return False
        if node_id in visited:
            return True

        visiting.add(node_id)
        _, left, right = nodes[node_id]

        for child in (left, right):
            if child != -1 and not dfs(child):
                return False

        visiting.remove(node_id)
        visited.add(node_id)
        return True

    if not dfs(root):
        return False, "ciclo detectado"

    if len(visited) != len(nodes):
        return False, "hay nodos no alcanzables"

    return True, "ok"


def traversals(nodes, root):
    preorder = []
    inorder = []
    postorder = []

    def dfs(node_id):
        if node_id == -1:
            return 0

        value, left, right = nodes[node_id]
        preorder.append(value)
        left_height = dfs(left)
        inorder.append(value)
        right_height = dfs(right)
        postorder.append(value)

        return 1 + max(left_height, right_height)

    height = dfs(root)
    return preorder, inorder, postorder, height


def solve():
    lines = [line.split() for line in sys.stdin.readlines() if line.split()]

    if not lines:
        return

    node_count = int(lines[0][0])
    nodes = {}

    for i in range(1, node_count + 1):
        node_id = int(lines[i][0])
        value = lines[i][1]
        left = int(lines[i][2])
        right = int(lines[i][3])
        nodes[node_id] = (value, left, right)

    root = int(lines[node_count + 1][0])
    valid, reason = validate_tree(nodes, root)

    print(f"valido = {'si' if valid else 'no'}")
    print(f"motivo = {reason}")

    if not valid:
        return

    preorder, inorder, postorder, height = traversals(nodes, root)
    print(f"nodos = {len(nodes)}")
    print(f"altura = {height}")
    print("preorder = " + " ".join(preorder))
    print("inorder = " + " ".join(inorder))
    print("postorder = " + " ".join(postorder))


if __name__ == "__main__":
    solve()
