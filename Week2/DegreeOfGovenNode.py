class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to find degree of a node
def find_degree(node):
    if not node:
        return 0
    degree = 0
    if node.left:
        degree += 1
    if node.right:
        degree += 1
    return degree

# Function to display each node and its degree
def display_node_degrees(root):
    if root:
        display_node_degrees(root.left)
        print(f"Node {root.data} has degree {find_degree(root)}")
        display_node_degrees(root.right)

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

# Display node degrees
print("Node degrees:")
display_node_degrees(root)
