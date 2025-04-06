def count_vertices_and_edges(graph):
    num_vertices = len(graph)
    num_edges = sum(len(neighbors) for neighbors in graph.values()) // 2  # For undirected graph
    return num_vertices, num_edges

# --- Take user input ---
graph = {}
n = int(input("Enter number of vertices: "))

for _ in range(n):
    node = input("Enter vertex label (e.g., A, B, C): ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

# --- Count vertices and edges ---
vertices, edges = count_vertices_and_edges(graph)
print(f"\nNumber of vertices: {vertices}")
print(f"Number of edges: {edges}")
