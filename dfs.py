def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')  # Print the visited node

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Get the number of nodes and edges from the user
num_nodes = int(input("Enter the number of nodes: "))
num_edges = int(input("Enter the number of edges: "))

# Initialize an empty graph
graph = {i: [] for i in range(num_nodes)}

# Input edges from the user
print("Enter each edge (start and end node, separated by space):")
for _ in range(num_edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # If the graph is undirected

# Input starting node for DFS
start_node = int(input("Enter the starting node: "))

# Perform DFS traversal
print("DFS traversal starting from node", start_node, ":")
dfs(graph, start_node)
