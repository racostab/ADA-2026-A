# Author: Ronquillo Nunez Braulio
# Minimum or Maximum Spanning Tree Problem

import sys


class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.rank = [0] * (size + 1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, first, second):
        root_first = self.find(first)
        root_second = self.find(second)

        if root_first == root_second:
            return False

        if self.rank[root_first] < self.rank[root_second]:
            self.parent[root_first] = root_second
        elif self.rank[root_first] > self.rank[root_second]:
            self.parent[root_second] = root_first
        else:
            self.parent[root_second] = root_first
            self.rank[root_first] += 1

        return True


def spanning_tree_weight(vertices, edges, tree_type):
    reverse = tree_type == "max"
    edges.sort(key=lambda edge: edge[2], reverse=reverse)

    disjoint_set = DisjointSet(vertices)
    total_weight = 0
    selected_edges = 0

    for first, second, weight in edges:
        if disjoint_set.union(first, second):
            total_weight += weight
            selected_edges += 1

            if selected_edges == vertices - 1:
                break

    return total_weight


def solve():
    data = sys.stdin.buffer.read().split()

    if not data:
        return

    pos = 0
    vertices = int(data[pos])
    pos += 1
    edge_count = int(data[pos])
    pos += 1
    tree_type = data[pos].decode()
    pos += 1

    edges = []
    for _ in range(edge_count):
        first = int(data[pos])
        pos += 1
        second = int(data[pos])
        pos += 1
        weight = int(data[pos])
        pos += 1
        edges.append((first, second, weight))

    sys.stdout.write(str(spanning_tree_weight(vertices, edges, tree_type)))


if __name__ == "__main__":
    solve()
