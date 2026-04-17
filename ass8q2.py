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

population_size = 50
generations = 200
mutation_rate = 0.1

def create_individual():
    p = list(range(1,n))
    random.shuffle(p)
    return [0] + p + [0]

def fitness(path):
    return 1 / cost(path)

def crossover(p1,p2):
    point = random.randint(1,n-2)

    child = p1[:point]
    for city in p2:
        if city not in child:
            child.append(city)

    child.append(0)
    return child

def mutate(path):
    if random.random() < mutation_rate:
        i,j = random.sample(range(1,n),2)
        path[i],path[j] = path[j],path[i]

population = [create_individual() for _ in range(population_size)]

for _ in range(generations):

    population.sort(key=cost)

    new_pop = population[:10]

    while len(new_pop) < population_size:
        p1,p2 = random.sample(population[:20],2)
        child = crossover(p1,p2)
        mutate(child)
        new_pop.append(child)

    population = new_pop

best = min(population,key=cost)

print("Best Path:",best)
print("Cost:",cost(best))
