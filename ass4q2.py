floor_plan = [
    ['1','1','1','1','1','1','1','1','1'],
    ['1','S','0','0','0','0','0','E','1'],
    ['1','0','1','1','1','1','0','0','1'],
    ['1','0','0','0','0','1','0','1','1'],
    ['1','1','1','1','0','0','0','1','1'],
    ['1','1','1','1','1','1','1','1','1']
]

def best_first_search_no_heuristic(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Find start and exit
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start = (i, j)
            if grid[i][j] == 'E':
                goal = (i, j)

    # Priority queue: (cost, (x, y), path)
    pq = [(0, start, [start])]
    visited = {}

    # Allowed moves: up, down, left, right
    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    while pq:
        # Manual priority queue (minimum cost first)
        pq.sort(key=lambda x: x[0])
        cost, (x, y), path = pq.pop(0)

        if (x, y) == goal:
            return path, cost

        if (x, y) in visited and visited[(x, y)] <= cost:
            continue

        visited[(x, y)] = cost

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] != '1':   # not a wall/room
                    pq.append(
                        (cost + 1, (nx, ny), path + [(nx, ny)])
                    )

    return None, None


path, total_cost = best_first_search_no_heuristic(floor_plan)

print("Evacuation Path:", path)
print("Total Steps:", total_cost)
