import heapq

class Node:
    def __init__(self, puzzle, move_count, parent=None):
        self.puzzle = puzzle
        self.move_count = move_count
        self.parent = parent
        self.blank_pos = puzzle.index(0)
        self.manhattan_distance = self.calculate_manhattan_distance()
        
    def calculate_manhattan_distance(self):
        distance = 0
        for i, tile in enumerate(self.puzzle):
            if tile != 0:
                goal_pos = tile - 1
                distance += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
        return distance
    
    def get_children(self):
        children = []
        row, col = self.blank_pos // 3, self.blank_pos % 3
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for r, c in moves:
            new_row, new_col = row + r, col + c
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_pos = new_row * 3 + new_col
                new_puzzle = self.puzzle[:]
                new_puzzle[self.blank_pos], new_puzzle[new_pos] = new_puzzle[new_pos], new_puzzle[self.blank_pos]
                children.append(Node(new_puzzle, self.move_count + 1, self))
        return children
    
    def __lt__(self, other):
        return (self.move_count + self.manhattan_distance) < (other.move_count + other.manhattan_distance)

def a_star(start_puzzle, goal_puzzle):
    start_node = Node(start_puzzle, 0)
    goal_node = Node(goal_puzzle, 0)
    
    open_list = []
    closed_list = set()
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.puzzle == goal_puzzle:
            path = []
            while current_node:
                path.append(current_node.puzzle)
                current_node = current_node.parent
            return path[::-1]
        
        closed_list.add(tuple(current_node.puzzle))
        
        for child in current_node.get_children():
            if tuple(child.puzzle) not in closed_list:
                heapq.heappush(open_list, child)
    
    return None

# Input from user
def get_puzzle_input(prompt):
    print(prompt)
    puzzle = []
    for i in range(3):
        row = input(f"Enter row {i + 1} (3 numbers separated by spaces, use 0 for blank): ").split()
        if len(row) != 3 or not all(num.isdigit() for num in row):
            raise ValueError("Each row must contain exactly 3 integers.")
        puzzle.extend(map(int, row))
    if sorted(puzzle) != list(range(9)):
        raise ValueError("Puzzle must contain all numbers from 0 to 8 exactly once.")
    return puzzle

try:
    start_puzzle = get_puzzle_input("Enter the starting puzzle:")
    goal_puzzle = get_puzzle_input("Enter the goal puzzle:")
    
    solution = a_star(start_puzzle, goal_puzzle)
    
    if solution:
        print("Solution found!")
        for step in solution:
            print(step[:3])
            print(step[3:6])
            print(step[6:])
            print()
    else:
        print("No solution exists.")
except ValueError as e:
    print(f"Input Error: {e}")
