class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to count internal (non-leaf) nodes
def count_internal_nodes(root):
    if not root or (not root.left and not root.right):
        return 0
    return 1 + count_internal_nodes(root.left) + count_internal_nodes(root.right)

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

# Display number of internal nodes
internal_count = count_internal_nodes(root)
print("Number of internal nodes:", internal_count)
