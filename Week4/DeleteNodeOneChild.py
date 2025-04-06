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

def delete_one_child_node(root, key):
    if not root:
        return root
    if key < root.data:
        root.left = delete_one_child_node(root.left, key)
    elif key > root.data:
        root.right = delete_one_child_node(root.right, key)
    else:
        # Node with only one child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# --- Main Execution ---
values = list(map(int, input("Enter BST elements: ").split()))
key = int(input("Enter node with one child to delete: "))
root = None
for val in values:
    root = insert_bst(root, val)

root = delete_one_child_node(root, key)
print("BST after deletion (in-order):")
inorder(root)
