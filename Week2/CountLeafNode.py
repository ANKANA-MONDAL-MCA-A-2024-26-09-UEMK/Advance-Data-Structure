class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to count leaf nodes
def count_leaf_nodes(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# Sample binary tree
'''
        A
       / \
      B   C
     / \   \
    D   E   F
'''

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

# Display number of leaf nodes
leaf_count = count_leaf_nodes(root)
print("Number of leaf nodes:", leaf_count)
