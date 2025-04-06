def count_odd_even_degrees(graph):
    odd = even = 0
    for node in graph:
        degree = len(graph[node])
        if degree % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even

# --- Take user input ---
graph = {}
n = int(input("Enter number of vertices: "))

for i in range(n):
    neighbors = list(map(int, input(f"Enter neighbors of vertex {i} (space-separated): ").split()))
    graph[i] = neighbors

# --- Count odd and even degree vertices ---
odd, even = count_odd_even_degrees(graph)
print(f"\nOdd degree vertices: {odd}")
print(f"Even degree vertices: {even}")
