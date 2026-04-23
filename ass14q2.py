def backward_chaining(rules, facts, goal, visited=None):
    if visited is None:
        visited = set()

    print("Trying to prove:", goal)

    # If goal is already a known fact
    if goal in facts:
        print(goal, "is a known fact.")
        return True

    # Avoid infinite loops
    if goal in visited:
        return False

    visited.add(goal)

    # Find rules where conclusion = goal
    for premise, conclusion in rules:
        if conclusion == goal:
            print("Checking rule:", premise, "->", conclusion)

            # Check all subgoals
            if all(backward_chaining(rules, facts, p, visited) for p in premise):
                print("Proved:", goal)
                return True

    print("Cannot prove:", goal)
    return False


# -------- PART (a) --------
rules_a = [
    (["P"], "Q"),
    (["R"], "Q"),
    (["A"], "P"),
    (["B"], "R")
]

facts_a = ["A", "B"]
goal_a = "Q"

print("---- Part (a) ----")
backward_chaining(rules_a, facts_a, goal_a)


# -------- PART (b) --------
rules_b = [
    (["A"], "B"),
    (["B", "C"], "D"),
    (["E"], "C")
]

facts_b = ["A", "E"]
goal_b = "D"

print("\n---- Part (b) ----")
backward_chaining(rules_b, facts_b, goal_b)