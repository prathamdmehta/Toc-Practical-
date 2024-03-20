def generate_derivation(production, start_symbol, max_derivations=10):
    derivations = [start_symbol]
    for i in range(max_derivations):
        next_derivation = ""
        for symbol in derivations[-1]:
            for prod in production:
                lhs, rhs = prod.split(" -> ")  # Corrected split
                if symbol == lhs:
                    next_derivation += rhs
        if next_derivation == "":
            break
        derivations.append(next_derivation)
    return derivations

production = ["S -> aSb", "S -> ab"]
start_symbol = "S"
print(generate_derivation(production, start_symbol))
