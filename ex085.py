oddOrEvenList = [[], []]
Values = 0
for Asks in range(1, 8):
    Values = int(input(f"Type the {Asks} value: "))
    if Values % 2 == 1:
        oddOrEvenList[1].append(Values)
    if Values % 2 == 0:
        oddOrEvenList[0].append(Values)
print("-="*40)
print(f"The odd values are {oddOrEvenList[1]}")
print(f"The even values are {oddOrEvenList[0]}")
