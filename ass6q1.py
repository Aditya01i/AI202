# Graph
graph = {
    "Chicago": [("Detroit", 283), ("Indianapolis", 182)],
    "Detroit": [("Chicago", 283), ("Buffalo", 256), ("Cleveland", 169)],
    "Indianapolis": [("Chicago", 182), ("Columbus", 176)],
    "Cleveland": [("Detroit", 169), ("Buffalo", 189), ("Pittsburgh", 134), ("Columbus", 144)],
    "Columbus": [("Indianapolis", 176), ("Cleveland", 144), ("Pittsburgh", 185)],
    "Pittsburgh": [("Cleveland", 134), ("Columbus", 185), ("Buffalo", 215), 
                   ("Syracuse", 253), ("Philadelphia", 305), ("Baltimore", 247)],
    "Buffalo": [("Detroit", 256), ("Cleveland", 189), ("Pittsburgh", 215), ("Syracuse", 150)],
    "Syracuse": [("Buffalo", 150), ("Pittsburgh", 253), ("New York", 254), ("Boston", 312)],
    "New York": [("Syracuse", 254), ("Philadelphia", 97), ("Providence", 181), ("Boston", 215)],
    "Philadelphia": [("Pittsburgh", 305), ("New York", 97), ("Baltimore", 101)],
    "Baltimore": [("Pittsburgh", 247), ("Philadelphia", 101)],
    "Providence": [("New York", 181), ("Boston", 50)],
    "Boston": []
}

# Heuristic to Boston
heuristic = {
    "Boston": 0,
    "Providence": 50,
    "Portland": 107,
    "New York": 215,
    "Philadelphia": 270,
    "Baltimore": 360,
    "Syracuse": 260,
    "Buffalo": 400,
    "Pittsburgh": 470,
    "Cleveland": 550,
    "Columbus": 640,
    "Detroit": 610,
    "Indianapolis": 780,
    "Chicago": 860
}


def greedy_best_first(start, goal):
    open_list = [start]
    visited = []
    parent = {}
    expanded = 0

    while open_list:
        # Select node with minimum heuristic
        current = min(open_list, key=lambda city: heuristic[city])
        open_list.remove(current)

        if current in visited:
            continue

        visited.append(current)
        expanded += 1

        if current == goal:
            break

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                open_list.append(neighbor)
                parent[neighbor] = current

    # Reconstruct path
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()

    return path, expanded


def a_star(start, goal):
    open_list = [start]
    visited = []
    parent = {}
    g_cost = {start: 0}
    expanded = 0

    while open_list:
        # Select node with minimum f(n) = g + h
        current = min(open_list, key=lambda city: g_cost[city] + heuristic[city])
        open_list.remove(current)

        if current in visited:
            continue

        visited.append(current)
        expanded += 1

        if current == goal:
            break

        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current
                if neighbor not in visited:
                    open_list.append(neighbor)

    # Reconstruct path
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()

    return path, expanded

start = "Chicago"
goal = "Boston"

g_path, g_expanded = greedy_best_first(start, goal)
a_path, a_expanded = a_star(start, goal)

print("Greedy Path:", g_path)
print("Cities Expanded (Greedy):", g_expanded)

print("\nA* Path:", a_path)
print("Cities Expanded (A*):", a_expanded)