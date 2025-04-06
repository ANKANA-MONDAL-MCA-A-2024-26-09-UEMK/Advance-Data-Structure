class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive insert function
def insert_recursive(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_recursive(root.left, data)
    else:
        root.right = insert_recursive(root.right, data)
    return root

# Inorder traversal to get sorted output
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# Main logic
nums = list(map(int, input("Enter numbers to sort using BST: ").split()))
sort_root = None
for num in nums:
    sort_root = insert_recursive(sort_root, num)

print("Sorted numbers using BST:")
inorder(sort_root)
