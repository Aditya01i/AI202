from itertools import product

# ----------------------------
# SYMBOL CLASS
# ----------------------------
class Symbol:
    def __init__(self, name):
        self.name = name

    def evaluate(self, values):
        return values[self.name]


# ----------------------------
# LOGIC OPERATIONS
# ----------------------------

class Not:
    def __init__(self, operand):
        self.operand = operand

    def evaluate(self, values):
        return not self.operand.evaluate(values)


class And:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, values):
        return self.left.evaluate(values) and self.right.evaluate(values)


class Or:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, values):
        return self.left.evaluate(values) or self.right.evaluate(values)


class Implies:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, values):
        return (not self.left.evaluate(values)) or self.right.evaluate(values)


class Biconditional:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, values):
        return self.left.evaluate(values) == self.right.evaluate(values)


# ----------------------------
# TRUTH TABLE FUNCTION
# ----------------------------
def truth_table(expr, symbols, title=""):
    names = [s.name for s in symbols]

    if title:
        print("\nExpression:", title)

    print("\t".join(names) + "\tResult")

    for values in product([False, True], repeat=len(symbols)):
        val_dict = dict(zip(names, values))

        result = expr.evaluate(val_dict)

        row = ["T" if v else "F" for v in values]
        row.append("T" if result else "F")

        print("\t".join(row))


# ----------------------------
# DEFINE SYMBOLS
# ----------------------------
P = Symbol('P')
Q = Symbol('Q')
R = Symbol('R')


# ----------------------------
# EXPRESSIONS (YOUR QUESTIONS)
# ----------------------------

# 1. ~P -> Q
expr1 = Implies(Not(P), Q)

# 2. P ∧ ~Q
expr2 = And(P, Not(Q))

# 3. ~P ∨ Q
expr3 = Or(Not(P), Q)

# 4. P -> Q
expr4 = Implies(P, Q)

# 5. P <-> Q
expr5 = Biconditional(P, Q)

# 6. (P ∨ Q) ∧ (~P -> Q)
expr6 = And(Or(P, Q), Implies(Not(P), Q))

# 7. (P ∨ Q) -> R
expr7 = Implies(Or(P, Q), R)

# 8. ((P ∨ Q) -> R) <-> ((~P ∧ ~Q) -> ~R)
expr8 = Biconditional(
    Implies(Or(P, Q), R),
    Implies(And(Not(P), Not(Q)), Not(R))
)

# 9. ((P -> Q) ∧ (Q -> R)) -> (P -> R)
expr9 = Implies(
    And(Implies(P, Q), Implies(Q, R)),
    Implies(P, R)
)

# 10. ((P -> (Q ∨ R)) -> (~P ∧ ~Q ∧ ~R))
expr10 = Implies(
    Implies(P, Or(Q, R)),
    And(And(Not(P), Not(Q)), Not(R))
)


# ----------------------------
# PRINT ALL TRUTH TABLES
# ----------------------------

truth_table(expr1, [P, Q], "~P -> Q")
truth_table(expr2, [P, Q], "P ∧ ~Q")
truth_table(expr3, [P, Q], "~P ∨ Q")
truth_table(expr4, [P, Q], "P -> Q")
truth_table(expr5, [P, Q], "P <-> Q")
truth_table(expr6, [P, Q], "(P ∨ Q) ∧ (~P -> Q)")
truth_table(expr7, [P, Q, R], "(P ∨ Q) -> R")
truth_table(expr8, [P, Q, R], "((P ∨ Q) -> R) <-> ((~P ∧ ~Q) -> ~R)")
truth_table(expr9, [P, Q, R], "((P -> Q) ∧ (Q -> R)) -> (P -> R)")
truth_table(expr10, [P, Q, R], "((P -> (Q ∨ R)) -> (~P ∧ ~Q ∧ ~R))")