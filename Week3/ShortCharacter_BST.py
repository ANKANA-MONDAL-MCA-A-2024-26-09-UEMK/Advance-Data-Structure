class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive insert function for BST
def insert_recursive(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_recursive(root.left, data)
    else:
        root.right = insert_recursive(root.right, data)
    return root

# Inorder traversal to display sorted characters
def inorder_char(root):
    if root:
        inorder_char(root.left)
        print(chr(root.data), end=' ')
        inorder_char(root.right)

# Input and build BST with characters of username
char_root = None
username = input("Enter your username: ").lower()

for ch in username:
    char_root = insert_recursive(char_root, ord(ch))  # convert char to ASCII

print("Sorted characters using BST:")
inorder_char(char_root)
