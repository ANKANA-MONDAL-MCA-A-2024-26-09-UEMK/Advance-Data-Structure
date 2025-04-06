class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert function to build BST
def insert_recursive(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_recursive(root.left, data)
    else:
        root.right = insert_recursive(root.right, data)
    return root

# Traversals
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

# Build the tree
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert_recursive(root, val)

# Perform traversals
print("In-order Traversal:")
inorder(root)
print("\nPre-order Traversal:")
preorder(root)
print("\nPost-order Traversal:")
postorder(root)
