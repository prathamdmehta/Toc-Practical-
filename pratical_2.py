def generate_regex(grammer):
    regex = " "
    for production in grammer:
        lhs , rhs = production.split("->")
        regex += "("+rhs+")"
    return regex
grammer = [ "S->aSb" , "S->ab",]
print(generate_regex(grammer))
