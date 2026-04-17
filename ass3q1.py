# Simple Reflex Agent for Vacuum Cleaner (3 Rooms)

# Environment: rooms and their status
environment = {
    "A": "Dirty",
    "B": "Dirty",
    "C": "Dirty"
}

# Rule Table using dictionary
rule_table = {
    ("A", "Dirty"): "Suck",
    ("A", "Clean"): "Move_Right",
    ("B", "Dirty"): "Suck",
    ("B", "Clean"): "Move_Right",
    ("C", "Dirty"): "Suck",
    ("C", "Clean"): "Move_Left"
}

# Initial location
current_location = "A"

print("Simulation Output:\n")

# Run until all rooms are clean
while "Dirty" in environment.values():

    # Percept
    status = environment[current_location]
    percept = (current_location, status)

    # Choose action from rule table
    action = rule_table[percept]

    # Print simulation step
    print(f"Percept: {percept}, Action: {action}, Location: {current_location}")

    # Perform action
    if action == "Suck":
        environment[current_location] = "Clean"

    elif action == "Move_Right":
        if current_location == "A":
            current_location = "B"
        elif current_location == "B":
            current_location = "C"

    elif action == "Move_Left":
        if current_location == "C":
            current_location = "B"
        elif current_location == "B":
            current_location = "A"

print("\nAll rooms are clean. Task completed!")
