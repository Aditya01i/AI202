# 5x5 Maze
# 0 = empty
# 1 = wall
# 2 = start
# 3 = reward

maze = [
    [2,0,0,0,1],
    [0,1,0,0,3],
    [0,3,0,1,1],
    [0,1,0,0,1],
    [3,0,0,0,3]
]

def a_star_maze(maze):
    rows = len(maze)
    cols = len(maze[0])

    # Find start and rewards
    rewards = []
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 2:
                start = (i, j)
            if maze[i][j] == 3:
                rewards.append((i, j))

    # Manhattan Distance Heuristic
    def heuristic(pos, remaining_rewards):
        if not remaining_rewards:
            return 0
        return min(abs(pos[0]-r[0]) + abs(pos[1]-r[1]) for r in remaining_rewards)

    # Open list: (position, g_cost, remaining_rewards)
    open_list = [(start, 0, tuple(rewards))]
    visited = set()
    parent = {}

    while open_list:

        # Select state with minimum f(n) = g + h
        current = min(open_list, 
                      key=lambda x: x[1] + heuristic(x[0], x[2]))
        open_list.remove(current)

        position, g_cost, remaining = current

        # Avoid revisiting same state
        if (position, remaining) in visited:
            continue

        visited.add((position, remaining))

        # Goal condition: all rewards collected
        if len(remaining) == 0:
            goal_state = current
            break

        x, y = position

        # Possible moves: Right, Left, Down, Up
        moves = [(0,1), (0,-1), (1,0), (-1,0)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] != 1:  # not a wall

                    new_remaining = list(remaining)

                    # If reward found, remove it
                    if (nx, ny) in new_remaining:
                        new_remaining.remove((nx, ny))

                    new_state = ((nx, ny), g_cost+1, tuple(new_remaining))

                    parent[new_state] = current
                    open_list.append(new_state)

    # Reconstruct path
    path = []
    state = goal_state

    while state in parent:
        path.append(state[0])
        state = parent[state]

    path.append(start)
    path.reverse()

    return path, visited, g_cost


# Run A*
path, visited, cost = a_star_maze(maze)

print("Final Path:")
print(path)

print("\nTotal Cost (Steps):", len(path)-1)

print("\nVisited States Count:", len(visited))