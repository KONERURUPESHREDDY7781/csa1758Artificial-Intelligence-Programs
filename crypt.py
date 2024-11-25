import itertools

def is_valid_solution(mapping, left_expr, right_expr):
    """
    Check if the given mapping satisfies the cryptarithm.
    """
    # Replace letters with corresponding digits
    for letter, digit in mapping.items():
        left_expr = left_expr.replace(letter, str(digit))
        right_expr = right_expr.replace(letter, str(digit))
    
    # Leading zero check
    if any(num.startswith('0') for num in left_expr.split('+')):
        return False
    if right_expr.startswith('0'):
        return False

    # Evaluate the expressions
    try:
        return eval(left_expr) == eval(right_expr)
    except:
        return False

def solve_cryptarithm(cryptarithm):
    """
    Solve the cryptarithm puzzle.
    """
    # Split into left and right expressions
    cryptarithm = cryptarithm.replace(" ", "")
    if '=' not in cryptarithm:
        print("Invalid format! Please include an '=' symbol.")
        return
    
    left_expr, right_expr = cryptarithm.split('=')

    # Extract unique letters
    unique_letters = set(filter(str.isalpha, cryptarithm))
    if len(unique_letters) > 10:
        print("Too many unique letters (maximum is 10).")
        return

    # Try all permutations of digits for the letters
    for perm in itertools.permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))

        if is_valid_solution(mapping, left_expr, right_expr):
            print("\nSolution found:")
            for letter, digit in mapping.items():
                print(f"{letter} = {digit}")
            return

    print("No solution found.")

def main():
    print("Cryptarithm Solver")
    print("Example: SEND + MORE = MONEY")
    cryptarithm = input("Enter the cryptarithm: ")
    solve_cryptarithm(cryptarithm)

if __name__ == "__main__":
    main()
