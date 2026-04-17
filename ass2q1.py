# Possible moves of blank tile
MOVES = {
    "U": -3,
    "D": 3,
    "L": -1,
    "R": 1
}

def is_valid_move(zero_pos, move):
    if move == "L" and zero_pos % 3 == 0:
        return False
    if move == "R" and zero_pos % 3 == 2:
        return False
    if move == "U" and zero_pos < 3:
        return False
    if move == "D" and zero_pos > 5:
        return False
    return True

def bfs_8_puzzle(start, goal):
    queue = []          # normal list as queue
    visited = set()

    queue.append(start)
    visited.add(start)

    states_explored = 0

    while queue:
        current = queue.pop(0)   # FIFO
        states_explored += 1

        if current == goal:
            print("Goal reached!")
            return states_explored

        zero_pos = current.index(0)

        for move in MOVES:
            if is_valid_move(zero_pos, move):
                new_pos = zero_pos + MOVES[move]
                new_state = list(current)

              
                new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)

    return -1  # goal not reachable

# Start and Goal states
start_state = (7, 2, 4,
               5, 0, 6,
               8, 3, 1)

goal_state = (0, 1, 2,
              3, 4, 5,
              6, 7, 8)

result = bfs_8_puzzle(start_state, goal_state)
print("States explored before reaching goal:", result)
