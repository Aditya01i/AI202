# Graph representation
graph = {
    "Chicago": {"Detroit": 283, "Cleveland": 345, "Indianapolis": 182},
    "Detroit": {"Chicago": 283, "Cleveland": 169, "Buffalo": 256},
    "Cleveland": {"Chicago": 345, "Detroit": 169, "Pittsburgh": 134, "Columbus": 144},
    "Indianapolis": {"Chicago": 182, "Columbus": 176},
    "Columbus": {"Indianapolis": 176, "Cleveland": 144, "Pittsburgh": 185},
    "Pittsburgh": {"Cleveland": 134, "Columbus": 185, "Philadelphia": 305, "Buffalo": 215},
    "Buffalo": {"Detroit": 256, "Pittsburgh": 215, "Syracuse": 150},
    "Syracuse": {"Buffalo": 150, "New York": 254, "Boston": 312},
    "Philadelphia": {"Pittsburgh": 305, "New York": 97},
    "New York": {"Philadelphia": 97, "Boston": 215},
    "Boston": {"New York": 215}
}

def uniform_cost_search(start, goal):
    # Priority queue as list: (cost, node, path)
    pq = [(0, start, [start])]
    visited = {}
    explored = 0

    while pq:
        # ---- Manual priority queue (min cost) ----
        pq.sort(key=lambda x: x[0])   # sort by cost
        cost, current, path = pq.pop(0)
        explored += 1

        if current == goal:
            return path, cost, explored

        if current in visited and visited[current] <= cost:
            continue

        visited[current] = cost
    
        for neighbor, edge_cost in graph[current].items():
            pq.append(
                (cost + edge_cost, neighbor, path + [neighbor])
            )

    return None, None, explored


path, total_cost, explored_nodes = uniform_cost_search("Chicago", "New York")

print("Path found:", path)
print("Total path cost:", total_cost)
print("Nodes explored:", explored_nodes)
