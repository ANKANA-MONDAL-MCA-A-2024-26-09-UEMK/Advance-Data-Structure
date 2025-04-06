from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to count sibling nodes
def count_siblings(root):
    if not root:
        return 0
    count = 0
    q = deque([root])
    while q:
        node = q.popleft()
        if node.left and node.right:
            count += 2  # both are siblings
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return count

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

# Display number of siblings
sibling_count = count_siblings(root)
print("Number of sibling nodes:", sibling_count)
