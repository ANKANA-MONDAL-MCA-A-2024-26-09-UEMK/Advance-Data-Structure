# Define the vertices
vertices = ['P', 'Q', 'R', 'S', 'T', 'U']
n = len(vertices)

# Create a mapping of vertex to index
vertex_index = {vertices[i]: i for i in range(n)}

# Initialize adjacency matrix with 0s
adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

# Define the edges based on the image (from → to, weight)
edges = [
    ('P', 'Q', 1),
    ('P', 'T', 7),
    ('Q', 'R', 1),
    ('Q', 'S', 6),
    ('R', 'U', 1),
    ('S', 'R', 2),
    ('S', 'U', 2),
    ('S', 'T', 3),
    ('T', 'U', 2),
    ('P', 'S', 4)
]

# Fill the adjacency matrix
for from_vertex, to_vertex, weight in edges:
    i = vertex_index[from_vertex]
    j = vertex_index[to_vertex]
    adj_matrix[i][j] = weight

# Display the adjacency matrix
print("Adjacency Matrix of the Directed Weighted Graph:\n")
print("   " + "  ".join(vertices))
for i in range(n):
    row = " ".join(f"{adj_matrix[i][j]:2}" for j in range(n))
    print(f"{vertices[i]}  {row}")
