class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to calculate the height of the binary tree
def tree_height(root):
    if not root:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

# Function to display the tree level-wise
def display_level_order(root):
    if not root:
        print("Tree is empty.")
        return

    from collections import deque
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Sample tree creation
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

# Display tree level-wise
print("Level-wise display of the tree:")
display_level_order(root)

# Display height of tree
print("\nHeight of the tree:", tree_height(root))
