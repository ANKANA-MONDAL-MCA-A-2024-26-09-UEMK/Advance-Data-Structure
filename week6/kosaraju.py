from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited, component)

    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_sccs(self):
        stack = []
        visited = [False] * self.V

        # Step 1: Fill stack with finishing order
        for i in range(self.V):
            if not visited[i]:
                self.fill_order(i, visited, stack)

        # Step 2: Get Transpose
        gr = self.transpose()

        # Step 3: DFS on transposed graph
        visited = [False] * self.V
        print("Strongly Connected Components are:")
        while stack:
            i = stack.pop()
            if not visited[i]:
                component = []
                gr.dfs_util(i, visited, component)
                print(component)

    def fill_order(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        stack.append(v)

# Example Usage
g1 = Graph(5)
g1.add_edge(1, 0)
g1.add_edge(0, 2)
g1.add_edge(2, 1)
g1.add_edge(0, 3)
g1.add_edge(3, 4)

g1.print_sccs()
