# States:
# location: 'A' or 'B'
# tile state: 'C' (clean), 'D' (dirty)

def goal_test(state):
    _, A, B = state
    return A == 'C' and B == 'C'


def actions(state):
    loc, A, B = state
    acts = ['Suck']
    
    if loc == 'A':
        acts.append('Right')
    else:
        acts.append('Left')
    
    return acts


# Non-deterministic result (returns LIST of states)
def result(state, action):
    loc, A, B = state
    
    if action == 'Suck':
        if loc == 'A':
            if A == 'D':
                # may clean A only OR both A and B
                return [
                    ('A', 'C', B),
                    ('A', 'C', 'C')
                ]
            else:
                # may make it dirty
                return [
                    ('A', 'D', B)
                ]
        
        elif loc == 'B':
            if B == 'D':
                return [
                    ('B', A, 'C'),
                    ('B', 'C', 'C')
                ]
            else:
                return [
                    ('B', A, 'D')
                ]
    
    elif action == 'Right':
        return [('B', A, B)]
    
    elif action == 'Left':
        return [('A', A, B)]


# AND-OR Search
def and_or_search(state):
    return or_search(state, [])


def or_search(state, path):
    if goal_test(state):
        return []

    if state in path:
        return None  # avoid loops

    for action in actions(state):
        results = result(state, action)
        plan = and_search(results, path + [state])
        
        if plan is not None:
            return (action, plan)

    return None


def and_search(states, path):
    plans = []
    
    for s in states:
        plan = or_search(s, path)
        if plan is None:
            return None
        plans.append(plan)
    
    return plans


# 🔹 Run Example
initial_state = ('A', 'D', 'D')

plan = and_or_search(initial_state)

print("Plan:", plan)