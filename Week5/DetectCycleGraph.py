def has_cycle(graph):
    visited = set()

    def dfs(v, parent):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:
                return True
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False

# --- User Input ---
graph = {}
n = int(input("Enter number of vertices: "))

for _ in range(n):
    node = int(input("Enter vertex: "))
    neighbors = list(map(int, input(f"Enter neighbors of {node} (space-separated): ").split()))
    graph[node] = neighbors

# --- Check for Cycle ---
print("Cycle Detected:" if has_cycle(graph) else "No Cycle Detected.")
