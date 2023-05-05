'''The code will basically run by asking
some values to the user and verifying if 
they are even or odd.'''

# Filtering the composite list to keep the even or odd values provided by the user.
oddOrEvenList = [[], []]
Values = 0

# Here i use "Loop for" to ask and verify if the response is even or odd.
for Asks in range(1, 8):
    Values = int(input(f"Type the {Asks} value: "))
    if Values % 2 == 1:
        oddOrEvenList[1].append(Values)
    if Values % 2 == 0:
        oddOrEvenList[0].append(Values)
        
# Final results.
print("-="*40)
print(f"The odd values are {oddOrEvenList[1]}")
print(f"The even values are {oddOrEvenList[0]}")
