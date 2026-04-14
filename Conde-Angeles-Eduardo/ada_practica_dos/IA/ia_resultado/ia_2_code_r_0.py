class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def binary_tree_sort(arr):
    if len(arr) == 0:
        return None

    # Create root node
    root = Node(arr[0])

    # Create binary tree
    for data in arr[1:]:
        insert(root, Node(data))

    # Perform inorder traversal
    result = []
    _inorder(root, result)

    return result

def insert(node, new_node):
    if node is None:
        node = new_node
    else:
        if node.data < new_node.data:
            if node.right is None:
                node.right = new_node
            else:
                insert(node.right, new_node)
        else:
            if node.left is None:
                node.left = new_node
            else:
                insert(node.left, new_node)

def _inorder(node, result):
    if node is not None:
        _inorder(node.left, result)
        result.append(node.data)
        _inorder(node.right, result)

def main():
    arr = list(map(int, input().split()))
    print(binary_tree_sort(arr))

if __name__ == "__main__":
    main()

# Test cases:
# 1. Input: 5 2 8 1 4 7 10
# 2. Output: [1, 2, 4, 5, 7, 8, 10]
# 3. Input: 3 6 9 1 10 2 11 5 7 8 4
# 4. Output: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
# 5. Input: 1 2 3 4 5 6 7 8 9 10
# 6. Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 7. Input: 10 9 8 7 6 5 4 3 2 1
# 8. Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 9. Input: 10 9 8 7 6 5 4 3 2 1 11 12 13 14 15
# 10. Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# 11. Input: 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
# 12. Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# 13. Input: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 14. Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# 15. Input: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 16 17 18 19 2