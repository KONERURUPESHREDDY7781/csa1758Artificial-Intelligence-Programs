import math

# Define a simple tree structure for testing
class GameNode:
    def __init__(self, label, value=None, children=None):
        self.label = label  # Node label (e.g., "A" for root)
        self.value = value  # Value only for leaf nodes
        self.children = children if children else []
    
    def is_terminal(self):
        # A node is terminal if it has no children
        return not self.children
    
    def evaluate(self):
        # Return the value of the node if it's a leaf
        return self.value
    
    def get_children(self):
        # Return the children of the node
        return self.children

# Function to implement Minimax Algorithm
def minimax(node, depth, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        max_eval = -math.inf
        for child in node.get_children():
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for child in node.get_children():
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

# Gather labels and values for the nodes from the user
root_label = input("Enter label for the root node (e.g., 'A'): ")
left_label = input("Enter label for the left intermediate node (e.g., 'B'): ")
right_label = input("Enter label for the right intermediate node (e.g., 'C'): ")

print("Please enter values for the four leaf nodes:")

# Gather input values from the user for each leaf node
leaf_values = []
for i in range(4):
    value = int(input(f"Enter value for leaf node {i+1}: "))
    leaf_values.append(GameNode(label=f"Leaf {i+1}", value=value))

# Build the tree based on user input
# Tree structure:
#         [root]
#        /       \
#   [left]       [right]
#   /     \      /      \
# leaf1  leaf2  leaf3  leaf4

# Level 2 nodes
left_child = GameNode(label=left_label, children=[leaf_values[0], leaf_values[1]])
right_child = GameNode(label=right_label, children=[leaf_values[2], leaf_values[3]])

# Level 1 root node
root = GameNode(label=root_label, children=[left_child, right_child])

# Run Minimax Algorithm
optimal_value = minimax(root, depth=2, maximizing_player=True)
print("Optimal Value:", optimal_value)

