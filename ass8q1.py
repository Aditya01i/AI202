import random

dist = [
[0,10,15,20,25,30,35,40],
[12,0,35,15,20,25,30,45],
[25,30,0,10,40,20,15,35],
[18,25,12,0,15,30,20,10],
[22,18,28,20,0,15,25,30],
[35,22,18,28,12,0,40,20],
[30,35,22,18,28,32,0,15],
[40,28,35,22,18,25,12,0]
]

n = 8

def cost(path):
    c = 0
    for i in range(len(path)-1):
        c += dist[path[i]][path[i+1]]
    return c

def random_path():
    p = list(range(1,n))
    random.shuffle(p)
    return [0] + p + [0]

def neighbors(path):
    neigh = []
    for i in range(1,n):
        for j in range(i+1,n):
            new = path[:]
            new[i],new[j] = new[j],new[i]
            neigh.append(new)
    return neigh

def beam_search(k, iterations=100):
    states = [random_path() for _ in range(k)]

    for _ in range(iterations):
        all_neighbors = []
        for s in states:
            all_neighbors.extend(neighbors(s))

        all_neighbors.sort(key=cost)
        states = all_neighbors[:k]

    best = min(states, key=cost)
    return best, cost(best)

for k in [3,5,10]:
    p,c = beam_search(k)
    print("k =",k,"Path:",p,"Cost:",c)