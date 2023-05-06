
# Variables and the List for a 3x3 matrix that will receive the values entered by the user.
matrixList = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sumEvenValues = highestValue2Line = columnSum = 0

# Loop to add the input response to the list.
for i in range(0, 3):
    for c in range(0, 3):
        matrixList[i][c] = int(input(f"Type a value for [{i}, {c}]: "))

# Final results. - Displaying the 3x3 matrix, assigning positions to each value and summing the even values. (Part 1).
print('\n', "-="*40, '\n')
for i in range(0, 3):
    for c in range(0, 3):
        print(f"[{matrixList[i][c]:^5}] ", end='')
        if matrixList[i][c] % 2 == 0:
            sumEvenValues += matrixList[i][c]
            
    print()

# Final Results (Part 2).
print('\n', "-="*40, '\n')
print(f"The sum of even values is {sumEvenValues}.")

# Loop summing the values of the third column.
for i in range(0, 3):
    columnSum += matrixList[i][2]
print(f"The sum of values in the third column is {columnSum}.")

# Loop to check the highest value in the second row.
for c in range(0, 3):
    if c == 0:
        highestValue2Line = matrixList[1][c]
    elif matrixList[1][c] > highestValue2Line:
        highestValue2Line = matrixList[1][c]
print(f"The largest value in the second row is {highestValue2Line}.")
