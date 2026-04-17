
graph = {
    "Raj": ["Priya", "Sunil"],
    "Priya": ["Raj", "Akash", "Neha", "Aarav"],
    "Sunil": ["Raj", "Akash", "Sneha"],
    "Akash": ["Priya", "Sunil"],
    "Neha": ["Priya", "Rahul"],
    "Aarav": ["Priya"],
    "Sneha": ["Sunil", "Maya", "Rahul"],
    "Rahul": ["Sneha", "Neha", "Pooja"],
    "Maya": ["Sneha"],
    "Pooja": ["Rahul", "Arjun"],
    "Arjun": ["Pooja"]
}


def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    print("BFS Traversal:  ")
    while queue:
        node = queue.pop(0)   # remove first element (FIFO)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


bfs(graph, "Raj")



def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


print(" \nDFS Traversal: ")
dfs(graph, "Raj")
