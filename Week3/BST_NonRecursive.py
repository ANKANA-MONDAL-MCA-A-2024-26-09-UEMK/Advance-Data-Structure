class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


def insert_non_recursive(root, data):
    if root is None:
        return Node(data)
    current = root
    while True:
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = Node(data)
                break
            current = current.right
    return root

# Example
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert_non_recursive(root, val)

print("\nBST Inorder Traversal (Non-Recursive Insert):")
inorder(root)
