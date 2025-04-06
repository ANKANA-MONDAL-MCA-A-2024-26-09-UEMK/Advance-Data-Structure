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

def delete_node(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        # Only delete if it's a leaf node
        if root.left is None and root.right is None:
            return None
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# --- Main Execution ---
values = list(map(int, input("Enter BST elements: ").split()))
key = int(input("Enter leaf node to delete: "))
root = None
for val in values:
    root = insert_bst(root, val)

root = delete_node(root, key)
print("BST after deletion (in-order):")
inorder(root)
