class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to count total nodes in the binary tree
def count_nodes_linked_list(root):
    if not root:
        return 0
    return 1 + count_nodes_linked_list(root.left) + count_nodes_linked_list(root.right)

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

# Display total number of nodes
total_nodes = count_nodes_linked_list(root)
print("Total number of nodes in the tree:", total_nodes)
