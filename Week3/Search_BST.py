class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

def search_bst(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search_bst(root.left, key)
    return search_bst(root.right, key)

# First build the BST
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert_non_recursive(root, val)

# Then perform the search
key = int(input("\nEnter element to search: "))
found = search_bst(root, key)
if found:
    print(f"{key} found in BST.")
else:
    print(f"{key} not found in BST.")
