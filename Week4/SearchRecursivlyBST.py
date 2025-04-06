class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_bst(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_bst(root.left, data)
    else:
        root.right = insert_bst(root.right, data)
    return root

def search_recursive(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search_recursive(root.left, key)
    else:
        return search_recursive(root.right, key)

# --- Main Execution ---
values = list(map(int, input("Enter BST elements (space separated): ").split()))
key = int(input("Enter key to search: "))
root = None
for val in values:
    root = insert_bst(root, val)

result = search_recursive(root, key)
print("Found ✅" if result else "Not Found ❌")
