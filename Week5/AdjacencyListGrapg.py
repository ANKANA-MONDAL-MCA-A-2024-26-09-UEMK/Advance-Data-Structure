# Define the graph using an adjacency list
graph = {
    'P': [('Q', 1), ('T', 7), ('S', 4)],
    'Q': [('R', 1), ('S', 6)],
    'R': [('U', 1)],
    'S': [('R', 2), ('U', 2), ('T', 3)],
    'T': [('U', 2)],
    'U': []
}

# Display the adjacency list
print("Adjacency List of the Directed Weighted Graph:\n")
for vertex in graph:
    edges = ", ".join([f"{neighbour}({weight})" for neighbour, weight in graph[vertex]])
    print(f"{vertex} -> {edges}")
