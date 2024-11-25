import itertools

def travelling_salesman(graph, start):
    # Get the number of nodes in the graph
    num_nodes = len(graph)
    
    # Generate all possible tours (excluding the starting node)
    nodes = list(range(num_nodes))
    nodes.remove(start)
    all_tours = itertools.permutations(nodes)
    
    # Find the minimum cost tour
    min_cost = float('inf')
    best_tour = None
    for tour in all_tours:
        # Add the starting point and return to the start
        tour_cost = graph[start][tour[0]] + sum(graph[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)) + graph[tour[-1]][start]
        
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = [start] + list(tour) + [start]
    
    return min_cost, best_tour

# Function to take user input for the graph
def input_graph():
    n = int(input("Enter the number of cities: "))
    print("Enter the adjacency matrix (use 0 for no direct path):")
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        graph.append(row)
    return graph

# Main execution
if __name__ == "__main__":
    # Input graph from user
    graph = input_graph()
    start_city = int(input("Enter the starting city (0-indexed): "))
    
    # Solve the TSP
    min_cost, best_tour = travelling_salesman(graph, start_city)
    
    # Output results
    print("\nMinimum cost:", min_cost)
    print("Best tour:", " -> ".join(map(str, best_tour)))
