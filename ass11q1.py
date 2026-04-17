# Adjacency list (example, you can expand this properly)
graph = {
    "Ahmedabad": ["Gandhinagar", "Kheda", "Mehsana"],
    "Gandhinagar": ["Ahmedabad", "Mehsana"],
    "Mehsana": ["Ahmedabad", "Gandhinagar"],
    "Kheda": ["Ahmedabad", "Vadodara"],
    "Vadodara": ["Kheda", "Bharuch"],
    "Bharuch": ["Vadodara", "Surat"],
    "Surat": ["Bharuch"]
}

colors = ["Red", "Green", "Blue", "Yellow"]

result = {}

def is_valid(node, color):
    for neighbor in graph[node]:
        if neighbor in result and result[neighbor] == color:
            return False
    return True

def solve():
    if len(result) == len(graph):
        return True
    
    node = list(graph.keys())[len(result)]
    
    for color in colors:
        if is_valid(node, color):
            result[node] = color
            
            if solve():
                return True
            
            del result[node]  # backtrack
    
    return False

solve()

print(result)