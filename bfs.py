 from collections import deque
def build_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges in the graph: "))
    print("Enter each edge as a pair of space-separated nodes (e.g., A B):")
    for _ in range(num_edges):
        node1, node2 = input().split()
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph
def bfs(graph, start_node):
    visited = set()             
    queue = deque([start_node])
    traversal_order = []        
    while queue: 
        node = queue.popleft() 
        if node not in visited:
          
            visited.add(node)
            traversal_order.append(node)
            
           
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return traversal_order

def main():
    print("Build the graph:")
    graph = build_graph()
    
    start_node = input("Enter the start node for BFS: ")
    
    if start_node not in graph:
        print("The start node is not in the graph.")
        return
    
    bfs_result = bfs(graph, start_node)
    print("BFS Traversal Order:", bfs_result)

main()
