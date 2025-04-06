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

# MAIN
nums = list(map(int, input("Enter space-separated integers for BST: ").split()))
root = None
for num in nums:
    root = insert_recursive(root, num)

print("In-order traversal of original BST:")
inorder(root)

new_val = int(input("\nEnter value to insert: "))
root = insert_recursive(root, new_val)

print("In-order traversal after insertion:")
inorder(root)
