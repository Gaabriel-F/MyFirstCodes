from time import sleep

# Define the Counter function with start, end, and step parameters.
def Counter(start, end, step):
    
    print('=-='*20)
    
    # Print the counting information.
    print(f'Counting from {start} to {end} jumping by {step}\n')
    
    # Check if counting is ascending or descending.
    if start < end:
        
        count = start
        
        # Perform ascending counting.
        while count <= end:
            
            # Print the current count.
            print(f'{count} ', end='', flush=True)
            
            sleep(0.3)
            
            # Increment the count by the step.
            count += step
        print('END!\n')
        
    else:
        
        count = start
        
        # Perform descending counting.
        while count >= end:
            
            # Print the current count.
            print(f'{count} ', end='', flush=True)
            
            sleep(0.3)
            
            # Decrement the count by the step.
            count -= step
            
        print('END!\n')
        
    print('=-='*20)

# Call the Counter function with specific arguments.
Counter(1, 10, 1)
Counter(10, 0, 2)

# Get input from the user to personalize the counting.
start = int(input('\nNow it\'s your turn to personalize the counting!\n\nStart: '))
end = int(input('End: '))
step = int(input('Step: '))

# Call the Counter function with user-defined arguments.
Counter(start, end, step)
