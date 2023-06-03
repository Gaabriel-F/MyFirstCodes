from random import randint
from time import sleep

# Create a function to draw 5 values and append them to a list.
def draw(tempList):
    print("DRAWING 5 VALUES INTO THE LIST: [ ", end='', flush=True)
    
    # Use an underscore (_) for a variable that won't be used.
    for _ in range(5):
        sleep(0.3)
        value = randint(1, 10)
        
        # Appending the values into the list and displaying them.
        # Please take note that the append operation is happening inside the for loop.
        tempList.append(value)
        print(f'{value} ', end='', flush=True)
        sleep(0.6)
        
    print('] DONE!')
    
    
# Create a function to display the list from the first function and calculate the sum of even values.
def sumEvenParameters(tempList):
    
    # Variable to sum the even values.
    totalSum = 0
    
    #Summing the even values.
    for num in tempList:
        if num % 2 == 0:
            totalSum += num
    
    # Displaying the list and the sum.
    print(f"Summing the even values of {tempList}, we get {totalSum}.")

    
# Main Program.
# Create a list to pass as a parameter into the draw() function and the sumEvenParameters() function.
listDrawnNumbers = []

# Calling the both functions in the main program.
draw(listDrawnNumbers)
sumEvenParameters(listDrawnNumbers)
