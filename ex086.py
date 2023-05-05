
#  List for a 3x3 matrix that will receive the values entered by the user.
matrixList = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Loop to add the input response to the list.
for i in range(0, 3):
    for c in range(0, 3):
        matrixList[i][c] = int(input(f"Type a value for [{i}, {c}]: "))

# Final results. - Displaying the 3x3 matrix and assigning positions to each value.
print('\n', "-="*40, '\n')
for i in range(0, 3):
    for c in range(0, 3):
        print(f"[{matrixList[i][c]:^5}] ", end='')
    print()
