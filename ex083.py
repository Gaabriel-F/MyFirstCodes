mathExpression = input("Type a math expression: ")
Character = []
for Symbols in mathExpression:

    # Validating this basic math expression
    if Symbols == "(":
        '''Here we check if the list starts with '('
        if it`s true, we go to line 15 and validate 
        that the list "Character" isn`t empty so we 
        remove the "(" from the list.'''
        Character.append("(")

    # If Character[Symbols] is ")" we check if the list is empty and then we remove the last item from them.
    elif Symbols == ")":
        if len(Character) > 0:
            Character.pop()
        # This happens when the list is incorrect. Here, I intentionally create an error and stop the loop.
        else:
            Character.append(")")
            break

#Final response to the user
if len(Character) == 0:
    print("This is a valid mathematical expression!")
else:
    print("This isn`t a valid mathematical expression!")
