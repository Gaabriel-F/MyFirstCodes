from time import sleep

# Create a function to receive parameters, determine the largest one, and analyze how many parameters were given to this function.
def highest( * numbers):
    
    # Separate line.
    print('=~'*40)
    
    # Informing the user about what will happen.
    print('\nAnalyzing the received values...\n')
    
    # Loop to print the values on the screen.
    for num in numbers:
        print(f'{num} ', end='', flush=True)
        sleep(0.5)
        
    # Displaying the datas about numbers quantity and highest value.
    print(f'\n\nThe total of {len(numbers)} values were reported.')
    
    # Adding a validation with an if condition in case the user doesn't provide any parameters to avoid errors.
    if len(numbers) != 0:
        print(f'The highest value reported was {max(numbers)}.\n')
    else:
        print(f'The highest value reported was 0.\n')
        
    # Separate line.
    print('=~'*40)
    print()
    
    
# Principal Program.

# Giving the parameters to the function.
highest(2, 4, 6)
highest(1, 99, 52, 8, 20)
highest(78, 2, 21, 43, 18, 9)
highest()
