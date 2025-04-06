def count_nodes_array(arr):
    return len([x for x in arr if x is not None])

# Array representation of binary tree (example with some None values)
# Index:      0    1    2    3    4    5    6
tree_array = ['A', 'B', 'C', 'D', 'E', None, 'F']

# Display total number of nodes
total_nodes = count_nodes_array(tree_array)
print("Total number of nodes in the array-based tree:", total_nodes)
