letters = ['S','E','N','D','M','O','R','Y']
used_digits = set()
assignment = {}

def solve(index):
    # If all letters assigned
    if index == len(letters):
        S = assignment['S']
        E = assignment['E']
        N = assignment['N']
        D = assignment['D']
        M = assignment['M']
        O = assignment['O']
        R = assignment['R']
        Y = assignment['Y']

        SEND = 1000*S + 100*E + 10*N + D
        MORE = 1000*M + 100*O + 10*R + E
        MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

        if SEND + MORE == MONEY:
            print("Solution found:")
            print(assignment)
            print(f"{SEND} + {MORE} = {MONEY}")
            return True
        return False

    # Pick current letter
    letter = letters[index]

    for digit in range(10):
        # Skip if already used
        if digit in used_digits:
            continue

        # Leading zero check
        if (letter == 'S' or letter == 'M') and digit == 0:
            continue

        # Choose
        assignment[letter] = digit
        used_digits.add(digit)

        # Recurse (try next letter)
        if solve(index + 1):
            return True

        # 🔙 Backtrack (undo)
        del assignment[letter]
        used_digits.remove(digit)

    return False

# Run
solve(0)