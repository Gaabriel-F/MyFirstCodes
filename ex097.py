def write(i):
    
    # Calculating the length of the input string and adding 2 for the border
    c = len(i) + 2
    
    # Printing the top border with "~" repeated c times
    print("~" * c)
    
    # Printing the input string with a space in front
    print(f' {i}')
    
    # Printing the bottom border with "~" repeated c times
    print("~" * c)
    
# Calling the write function with those inputs.
write('Hello World')
write('Writing')
write('I\'m the number one!')
