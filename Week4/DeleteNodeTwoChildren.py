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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete_two_children_node(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete_two_children_node(root.left, key)
    elif key > root.data:
        root.right = delete_two_children_node(root.right, key)
    else:
        # Node with two children
        if root.left and root.right:
            temp = min_value_node(root.right)
            root.data = temp.data
            root.right = delete_two_children_node(root.right, temp.data)
        elif root.left:
            return root.left
        elif root.right:
            return root.right
        else:
            return None
    return root

# --- Main Execution ---
values = list(map(int, input("Enter BST elements: ").split()))
key = int(input("Enter node with two children to delete: "))
root = None
for val in values:
    root = insert_bst(root, val)

root = delete_two_children_node(root, key)
print("BST after deletion (in-order):")
inorder(root)
