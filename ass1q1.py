#BFS 


graph = {
    "Chicago": {"Detroit": 283, "Cleveland": 345, "Indianapolis": 182},
    "Detroit": {"Chicago": 283, "Buffalo": 256, "Cleveland": 169},
    "Buffalo": {"Detroit": 256, "Syracuse": 150},
    "Syracuse": {"Buffalo": 150, "Boston": 312, "New York": 254},
    "Boston": {"Syracuse": 312, "New York": 215, "Portland": 107, "Providence": 50},
    "Portland": {"Boston": 107},
    "Providence": {"Boston": 50, "New York": 181},
    "New York": {"Syracuse": 254, "Boston": 215, "Providence": 181, "Philadelphia": 97},
    "Philadelphia": {"New York": 97, "Baltimore": 101, "Pittsburgh": 305},
    "Baltimore": {"Philadelphia": 101, "Columbus": 247},
    "Columbus": {"Baltimore": 247, "Cleveland": 144, "Indianapolis": 176, "Pittsburgh": 185},
    "Cleveland": {"Chicago": 345, "Detroit": 169, "Columbus": 144, "Pittsburgh": 134},
    "Pittsburgh": {"Cleveland": 134, "Columbus": 185, "Philadelphia": 305},
    "Indianapolis": {"Chicago": 182, "Columbus": 176}
}


def bfs_all_paths(start, goal):
    queue = [(start, [start], 0)]   # normal list
    results = []

    while queue:
        current, path, cost = queue.pop(0)   # FIFO behavior

        if current == goal:
            results.append((path, cost))
            continue

        for neighbor, dist in graph[current].items():
            if neighbor not in path:   # avoid cycles
                queue.append((neighbor, path + [neighbor], cost + dist))

    return results


start = "Syracuse"
goal = "Chicago"

print("\nBFS Paths:\n")
bfs_paths = bfs_all_paths(start, goal)

for p, c in bfs_paths:
    print(" -> ".join(p), "| Cost =", c)



#DFS
def dfs_all_paths(start, goal, path=None, cost=0):
    if path is None:
        path = [start]
    else:
        path = path + [start]

    if start == goal:
        return [(path, cost)]

    paths = []
    for neighbor, dist in graph[start].items():
        if neighbor not in path:  # avoid cycles
            new_paths = dfs_all_paths(neighbor, goal, path, cost + dist)
            for p in new_paths:
                paths.append(p)

    return paths


start = "Syracuse"
goal = "Chicago"


print("\nDFS Paths:\n")

results = dfs_all_paths(start, goal)

for p, c in results:
    print(" -> ".join(p), "| Cost =", c)
