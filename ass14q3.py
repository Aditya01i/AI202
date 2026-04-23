def resolve(c1, c2):
    resolvents = []
    for literal in c1:
        if '-' + literal in c2:
            new_clause = (c1 - {literal}) | (c2 - {'-' + literal})
            resolvents.append(new_clause)
        elif literal.startswith('-') and literal[1:] in c2:
            new_clause = (c1 - {literal}) | (c2 - {literal[1:]})
            resolvents.append(new_clause)
    return resolvents


def resolution(kb, query):
    clauses = kb.copy()
    clauses.append({'-' + query})

    new = []

    while True:
        pairs = [(clauses[i], clauses[j]) for i in range(len(clauses)) for j in range(i+1, len(clauses))]

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            if set() in resolvents:
                return True
            new.extend(resolvents)

        if all(clause in clauses for clause in new):
            return False

        for clause in new:
            if clause not in clauses:
                clauses.append(clause)


# Example for (a)
kb = [
    {'P', 'Q'},
    {'-P', 'R'},
    {'-Q', 'S'},
    {'-R', 'S'}
]

print("Conclusion S is:", resolution(kb, 'S'))