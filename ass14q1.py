def forward_chaining(rules, facts, goal):
    inferred = set(facts)

    while True:
        new_inferred = set()

        for premise, conclusion in rules:
            # check if all premises are satisfied
            if all(p in inferred for p in premise):
                if conclusion not in inferred:
                    new_inferred.add(conclusion)

        if not new_inferred:
            break

        inferred.update(new_inferred)

        print("New facts inferred:", new_inferred)

        if goal in inferred:
            print("\nGoal", goal, "reached!")
            return True

    print("\nGoal not reached.")
    return False


# -------- PART (a) --------
rules_a = [
    (["P"], "Q"),
    (["L", "M"], "P"),
    (["A", "B"], "L")
]

facts_a = ["A", "B", "M"]
goal_a = "Q"

print("---- Part (a) ----")
forward_chaining(rules_a, facts_a, goal_a)


# -------- PART (b) --------
rules_b = [
    (["A"], "B"),
    (["B"], "C"),
    (["C"], "D"),
    (["D", "E"], "F")
]

facts_b = ["A", "E"]
goal_b = "F"

print("\n---- Part (b) ----")
forward_chaining(rules_b, facts_b, goal_b)