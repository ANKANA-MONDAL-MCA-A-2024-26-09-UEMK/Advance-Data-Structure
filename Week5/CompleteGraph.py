def is_complete_graph(graph):
    n = len(graph)
    for node in graph:
        if len(graph[node]) != n - 1:
            return False
    return True

# --- User Input ---
graph = {}
n = int(input("Enter number of vertices: "))

for i in range(n):
    neighbors = list(map(int, input(f"Enter neighbors of vertex {i} (space-separated): ").split()))
    graph[i] = neighbors

# --- Check Completeness ---
print("The graph is complete." if is_complete_graph(graph) else "The graph is not complete.")
