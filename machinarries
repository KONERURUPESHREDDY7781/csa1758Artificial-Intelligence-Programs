from collections import deque
def is_valid_state(m_left, c_left, b_left, m_total=3, c_total=3):
    m_right = m_total - m_left
    c_right = c_total - c_left
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False
    return True
def get_successors(m_left, c_left, b_left):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    successors = []
    for m, c in moves:
        if b_left == 1:  
            new_state = (m_left - m, c_left - c, 0)
        else:  
            new_state = (m_left + m, c_left + c, 1)
        if is_valid_state(new_state[0], new_state[1], new_state[2]):
            successors.append(new_state)
    return successors
def solve_missionaries_cannibals():
    initial_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    while queue:
        (m_left, c_left, b_left), path = queue.popleft()
        if (m_left, c_left, b_left) == goal_state:
            path.append((m_left, c_left, b_left))
            return path
        for successor in get_successors(m_left, c_left, b_left):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [(m_left, c_left, b_left)]))
    return None
solution = solve_missionaries_cannibals()
if solution:
    print("Solution found:")
    for state in solution:
        print(f"Left Bank: Missionaries={state[0]}, Cannibals={state[1]}, Boat={'Left' if state[2] == 1 else 'Right'}")
else:
    print("No solution exists.")
