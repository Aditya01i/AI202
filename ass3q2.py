# Simple Reflex Agent for Indian Railways Level Crossing

def level_crossing_agent(inbound, outbound, obstacle, manual):
    """
    inbound  : True / False
    outbound : True / False
    obstacle : True / False
    manual   : True / False
    """

    # Rule Priority 1: Manual Emergency
    if manual:
        return {
            "Gate": "Lower",
            "Hooter": "On",
            "Train Signal": "Red",
            "Location": "Control Room (Manual Override)"
        }

    # Rule Priority 2: Obstacle on crossing
    if obstacle:
        return {
            "Gate": "Lower",
            "Hooter": "On",
            "Train Signal": "Red",
            "Location": "On the Level Crossing"
        }

    # Rule Priority 3: Train detected
    if inbound or outbound:
        return {
            "Gate": "Lower",
            "Hooter": "On",
            "Train Signal": "Green",
            "Location": "Before the Level Crossing"
        }

    # Rule Priority 4: Normal condition
    return {
        "Gate": "Raise",
        "Hooter": "Off",
        "Train Signal": "Green",
        "Location": "Normal Road Operation"
    }


# ------------------ Simulation ------------------

test_cases = [
    ("Train approaching, road clear", True, False, False, False),
    ("Obstacle on road", False, False, True, False),
    ("Manual emergency activated", False, False, False, True),
    ("No train, no obstacle", False, False, False, False),
    ("Both tracks active", True, True, False, False),
]

for desc, inbound, outbound, obstacle, manual in test_cases:
    action = level_crossing_agent(inbound, outbound, obstacle, manual)

    print("\nScenario:", desc)
    print("Percepts:")
    print("  Inbound Track :", inbound)
    print("  Outbound Track:", outbound)












    
    print("  Obstacle      :", obstacle)
    print("  Manual Input  :", manual)

    print("Actions:")
    for k, v in action.items():
        print(f"  {k}: {v}")
