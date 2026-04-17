TOTAL = 3
GOAL = (0, 0, 1)

# ----------------------------
# Check if state is valid
# ----------------------------
def is_valid(GL, BL):
    GR = TOTAL - GL
    BR = TOTAL - BL

    if GL < 0 or BL < 0 or GL > TOTAL or BL > TOTAL:
        return False

    # Left side condition
    if GL > 0 and BL > GL:
        return False

    # Right side condition
    if GR > 0 and BR > GR:
        return False

    return True


# ----------------------------
# Generate Successors
# ----------------------------
def get_successors(state):
    GL, BL, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    successors = []

    for g, b in moves:
        if boat == 0:  # boat on left
            new_state = (GL - g, BL - b, 1)
        else:          # boat on right
            new_state = (GL + g, BL + b, 0)

        if is_valid(new_state[0], new_state[1]):
            successors.append(new_state)

    return successors


# ----------------------------
# Depth Limited Search (Recursive)
# ----------------------------
def dls(state, depth, limit, path, explored_count):
    explored_count[0] += 1

    if state == GOAL:
        return path

    if depth == limit:
        return None

    for next_state in get_successors(state):
        if next_state not in path:   # avoid cycles
            result = dls(next_state,
                         depth + 1,
                         limit,
                         path + [next_state],
                         explored_count)
            if result:
                return result

    return None


def depth_limited_search(limit):
    explored_count = [0]
    result = dls((3,3,0), 0, limit, [(3,3,0)], explored_count)
    return result, explored_count[0]


# ----------------------------
# Iterative Deepening Search
# ----------------------------
def iterative_deepening():
    total_explored = 0
    depth = 0

    while True:
        result, explored = depth_limited_search(depth)
        total_explored += explored

        if result:
            return result, total_explored, depth

        depth += 1


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":

    print("Depth Limited Search (limit = 3)")
    result, explored = depth_limited_search(3)

    if result:
        print("Solution:", result)
    else:
        print("No solution within depth 3")

    print("States explored:", explored)

    print("\nIterative Deepening Search")
    solution, total_explored, depth = iterative_deepening()

    print("Solution depth:", depth)
    print("Solution path:")
    for step in solution:
        print(step)

    print("Total states explored:", total_explored)
