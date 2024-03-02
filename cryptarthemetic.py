import itertools
def solve_cryptarithmetic(puzzle):
    unique_letters = set(ch for ch in puzzle if ch.isalpha())
    digit_permutations = itertools.permutations(range(10), len(unique_letters))
    for perm in digit_permutations:
        mapping = dict(zip(unique_letters, perm))
        left_value, right_value = evaluate_puzzle(puzzle, mapping)
        if left_value == right_value:
            return mapping, left_value
    return None, None
def evaluate_puzzle(puzzle, mapping):
    translated_puzzle = ''.join(str(mapping.get(ch, ch)) for ch in puzzle)
    terms = translated_puzzle.split("==")
    if len(terms) != 2:
        return None, None
    left_term, right_term = terms[0], terms[1]
    left_value = evaluate_expression(left_term)
    right_value = evaluate_expression(right_term)
    return left_value, right_value
def evaluate_expression(expression):
    value = 0
    components = expression.strip().split()
    for component in components:
        if component.isnumeric():
            value += int(component)
    return value
puzzle = "SEND + MORE == MONEY"
solution, final_value = solve_cryptarithmetic(puzzle)
if solution:
    print("Solution found:")
    for key, value in solution.items():
        print(key, "=", value)
    print("Final calculated value:", final_value)
else:
    print("No solution found.")
