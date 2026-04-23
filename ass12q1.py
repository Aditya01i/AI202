# Variables
variables = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']

# Domains
domains = {
    var: ['R1', 'R2', 'R3'] for var in variables
}

# Constraints (neighbors)
constraints = {
    'P1': ['P2', 'P3', 'P6'],
    'P2': ['P1', 'P3', 'P4'],
    'P3': ['P1', 'P2', 'P5'],
    'P4': ['P2', 'P6'],
    'P5': ['P3', 'P6'],
    'P6': ['P1', 'P4', 'P5']
}

# Constraint function (Xi ≠ Xj)
def constraint(x, y):
    return x != y

# Revise function
def revise(domains, xi, xj):
    revised = False
    for x in domains[xi][:]:  # copy to avoid runtime issues
        valid = False
        for y in domains[xj]:
            if constraint(x, y):
                valid = True
                break
        if not valid:
            domains[xi].remove(x)
            revised = True
    return revised

# AC-3 without deque
def ac3(domains):
    queue = []

    # Initialize queue
    for xi in constraints:
        for xj in constraints[xi]:
            queue.append((xi, xj))

    steps = 0

    while queue:
        xi, xj = queue.pop(0)  # FIFO queue using list

        print(f"Checking arc ({xi}, {xj})")

        if revise(domains, xi, xj):
            print(f"Updated domain: {xi} -> {domains[xi]}")

            if len(domains[xi]) == 0:
                return False

            for xk in constraints[xi]:
                if xk != xj:
                    queue.append((xk, xi))

        steps += 1
        if steps == 5:
            print("---- First 5 arc checks done ----")

    return True


# -------- RUN 1: Initial AC-3 --------
print("Initial AC-3:")
ac3(domains)
print("Domains:", domains)


# -------- RUN 2: Assign P1 = R1 --------
domains['P1'] = ['R1']

print("\nAfter assigning P1 = R1:")
result = ac3(domains)

print("Final Domains:", domains)
print("Is consistent?", result)