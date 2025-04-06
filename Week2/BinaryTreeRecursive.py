from collections import deque

# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive function to create the binary tree
def insert_recursive():
    data = input("Enter node data (or 'None' to skip): ")
    if data.lower() == 'none':
        return None
    try:
        node = Node(int(data))
    except ValueError:
        print("Invalid input! Please enter an integer or 'None'.")
        return insert_recursive()

    print(f"Enter left child of {node.data}:")
    node.left = insert_recursive()
    print(f"Enter right child of {node.data}:")
    node.right = insert_recursive()
    return node

# Function to display the tree level-wise
def level_order(root):
    if not root:
        print("Tree is empty.")
        return
    print("\nLevel Order Traversal:")
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print()

def insert_sample_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(6)
    return root

root = insert_sample_tree()
level_order(root)

# Main Program
if __name__ == "__main__":
    print("=== Binary Tree Creation using Recursion ===")
    root = insert_recursive()
    level_order(root)
