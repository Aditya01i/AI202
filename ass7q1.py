import random
import math

N = 8

# -------------------------------
# Generate Random Board
# -------------------------------
def random_board():
    return [random.randint(0, N-1) for _ in range(N)]


# -------------------------------
# Heuristic Function
# h(n) = number of attacking pairs
# -------------------------------
def heuristic(board):
    attacks = 0
    for i in range(N):
        for j in range(i+1, N):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                attacks += 1
    return attacks


# -------------------------------
# Generate Neighbours
# -------------------------------
def get_neighbors(board):
    neighbors = []

    for col in range(N):
        for row in range(N):
            if row != board[col]:
                new_board = board.copy()
                new_board[col] = row
                neighbors.append(new_board)

    return neighbors


# -------------------------------
# Steepest Ascent Hill Climbing
# -------------------------------
def steepest_ascent(board):

    steps = 0
    current = board
    current_h = heuristic(current)

    while True:

        neighbors = get_neighbors(current)

        best_neighbor = None
        best_h = current_h

        for n in neighbors:
            h = heuristic(n)
            if h < best_h:
                best_h = h
                best_neighbor = n

        if best_neighbor is None:
            break

        current = best_neighbor
        current_h = best_h
        steps += 1

        if current_h == 0:
            break

    return heuristic(board), current_h, steps, ("Solved" if current_h == 0 else "Fail")


# -------------------------------
# First Choice Hill Climbing
# -------------------------------
def first_choice(board):

    steps = 0
    current = board
    current_h = heuristic(current)

    while True:

        neighbors = get_neighbors(current)
        random.shuffle(neighbors)

        found = False

        for n in neighbors:
            if heuristic(n) < current_h:
                current = n
                current_h = heuristic(n)
                steps += 1
                found = True
                break

        if not found or current_h == 0:
            break

    return heuristic(board), current_h, steps, ("Solved" if current_h == 0 else "Fail")


# -------------------------------
# Random Restart Hill Climbing
# -------------------------------
def random_restart(max_restart=50):

    total_steps = 0

    for r in range(max_restart):

        board = random_board()
        initial_h, final_h, steps, status = steepest_ascent(board)

        total_steps += steps

        if status == "Solved":
            return initial_h, final_h, total_steps, "Solved"

    return initial_h, final_h, total_steps, "Fail"


# -------------------------------
# Simulated Annealing
# -------------------------------
def simulated_annealing(board):

    current = board
    current_h = heuristic(current)
    T = 100
    cooling = 0.95
    steps = 0

    while T > 0.1 and current_h != 0:

        neighbors = get_neighbors(current)
        next_state = random.choice(neighbors)

        next_h = heuristic(next_state)

        delta = next_h - current_h

        if delta < 0:
            current = next_state
            current_h = next_h

        else:
            prob = math.exp(-delta / T)
            if random.random() < prob:
                current = next_state
                current_h = next_h

        T *= cooling
        steps += 1

    return heuristic(board), current_h, steps, ("Solved" if current_h == 0 else "Fail")


# ======================================
# Run Experiment (50 Random Boards)
# ======================================

runs = 50

print("\nSTEPEST ASCENT HILL CLIMBING")
print("Run | Initial h | Final h | Steps | Status")

for i in range(runs):
    board = random_board()
    result = steepest_ascent(board)
    print(i+1, result)


print("\nFIRST CHOICE HILL CLIMBING")
print("Run | Initial h | Final h | Steps | Status")

for i in range(runs):
    board = random_board()
    result = first_choice(board)
    print(i+1, result)


print("\nRANDOM RESTART HILL CLIMBING")
print("Run | Initial h | Final h | Steps | Status")

for i in range(runs):
    result = random_restart()
    print(i+1, result)


print("\nSIMULATED ANNEALING")
print("Run | Initial h | Final h | Steps | Status")

for i in range(runs):
    board = random_board()
    result = simulated_annealing(board)
    print(i+1, result)