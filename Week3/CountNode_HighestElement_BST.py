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

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def find_max(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.data

# Build the BST
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert_recursive(root, val)

# Count nodes and find highest
total_nodes = count_nodes(root)
max_element = find_max(root)

print(f"\nTotal number of nodes: {total_nodes}")
print(f"Highest element in BST: {max_element}")
