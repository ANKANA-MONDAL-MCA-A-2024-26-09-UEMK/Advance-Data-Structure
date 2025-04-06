from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, data_list):
        if not data_list:
            return
        self.root = Node(data_list[0])
        q = deque([self.root])
        i = 1
        while i < len(data_list):
            curr = q.popleft()
            if data_list[i] is not None:
                curr.left = Node(data_list[i])
                q.append(curr.left)
            i += 1
            if i < len(data_list) and data_list[i] is not None:
                curr.right = Node(data_list[i])
                q.append(curr.right)
            i += 1

    def display_level_order(self):
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.data, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

bt = BinaryTree()
bt.insert_level_order([1, 2, 3, None, 5, 6, 7])
bt.display_level_order()
