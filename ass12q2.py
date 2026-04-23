# Convert input string to grid
def parse_grid(grid_str):
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            val = int(grid_str[i*9 + j])
            if val == 0:
                row.append([1,2,3,4,5,6,7,8,9])
            else:
                row.append([val])
        grid.append(row)
    return grid


# Get neighbors (row, column, box)
def get_neighbors(r, c):
    neighbors = set()

    # Row + Column
    for i in range(9):
        if i != c:
            neighbors.add((r, i))
        if i != r:
            neighbors.add((i, c))

    # Box
    br = (r // 3) * 3
    bc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            nr, nc = br+i, bc+j
            if (nr, nc) != (r, c):
                neighbors.add((nr, nc))

    return list(neighbors)


# Revise function
def revise(grid, xi, xj):
    r1, c1 = xi
    r2, c2 = xj

    revised = False

    for val in grid[r1][c1][:]:
        valid = False
        for v2 in grid[r2][c2]:
            if val != v2:
                valid = True
                break
        if not valid:
            grid[r1][c1].remove(val)
            revised = True

    return revised


# AC-3 Algorithm
def ac3(grid):
    queue = []

    # Generate all arcs
    for r in range(9):
        for c in range(9):
            for neighbor in get_neighbors(r, c):
                queue.append(((r, c), neighbor))

    removed_count = 0

    while queue:
        (xi, xj) = queue.pop(0)

        if revise(grid, xi, xj):
            removed_count += 1

            r, c = xi
            if len(grid[r][c]) == 0:
                return False, removed_count

            for neighbor in get_neighbors(r, c):
                if neighbor != xj:
                    queue.append((neighbor, xi))

    return True, removed_count


# Print domain sizes
def print_domain_sizes(grid):
    for r in range(9):
        for c in range(9):
            print(len(grid[r][c]), end=" ")
        print()


# ---------------- MAIN ----------------

grid_str = (
    "000006000"
    "059000008"
    "200008000"
    "045000000"
    "003000000"
    "006003050"
    "000070000"
    "000000000"
    "000050002"
)

grid = parse_grid(grid_str)

result, removed = ac3(grid)

print("Arc Consistent:", result)
print("Values removed:", removed)

print("\nDomain sizes after AC-3:")
print_domain_sizes(grid)