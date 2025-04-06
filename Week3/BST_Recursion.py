class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_recursive(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_recursive(root.left, data)
    else:
        root.right = insert_recursive(root.right, data)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# Example
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert_recursive(root, val)

print("BST Inorder Traversal (Recursive):")
inorder(root)
