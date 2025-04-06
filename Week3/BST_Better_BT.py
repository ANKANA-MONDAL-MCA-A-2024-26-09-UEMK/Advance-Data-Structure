import time

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Binary Tree - Insert level-wise (not sorted)
def insert_bt(root, data_list):
    from collections import deque
    if not data_list:
        return None
    root = Node(data_list[0])
    q = deque([root])
    i = 1
    while i < len(data_list):
        curr = q.popleft()
        if i < len(data_list) and data_list[i] is not None:
            curr.left = Node(data_list[i])
            q.append(curr.left)
        i += 1
        if i < len(data_list) and data_list[i] is not None:
            curr.right = Node(data_list[i])
            q.append(curr.right)
        i += 1
    return root

# Binary Tree search (brute-force)
def search_bt(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    return search_bt(root.left, key) or search_bt(root.right, key)

# BST insert
def insert_bst(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_bst(root.left, data)
    else:
        root.right = insert_bst(root.right, data)
    return root

# BST search with comparison count
def search_bst(root, key, count=0):
    if root is None:
        return False, count
    count += 1
    if root.data == key:
        return True, count
    elif key < root.data:
        return search_bst(root.left, key, count)
    else:
        return search_bst(root.right, key, count)

# Main
data = [50, 30, 70, 20, 40, 60, 80]
search_key = 80

# Binary Tree
bt_root = insert_bt(None, data)
start_bt = time.time()
found_bt = search_bt(bt_root, search_key)
end_bt = time.time()
bt_time = (end_bt - start_bt) * 1000

# BST
bst_root = None
for d in data:
    bst_root = insert_bst(bst_root, d)

start_bst = time.time()
found_bst, comparisons = search_bst(bst_root, search_key)
end_bst = time.time()
bst_time = (end_bst - start_bst) * 1000

# Output
print("=== Comparison: Binary Tree vs Binary Search Tree ===")
print(f"Searching for {search_key} in Binary Tree: {'Found' if found_bt else 'Not Found'}")
print(f"Time taken (BT): {bt_time:.6f} ms")

print(f"\nSearching for {search_key} in Binary Search Tree: {'Found' if found_bst else 'Not Found'}")
print(f"Time taken (BST): {bst_time:.6f} ms")
print(f"Comparisons in BST: {comparisons}")

print("\n✅ Conclusion:")
print("Binary Search Tree is more efficient than Binary Tree for search operations.")
print("Because it reduces the number of comparisons and has better time complexity (O(log n) vs O(n)) in ideal cases.")
