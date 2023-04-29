NumbersList = []
for Loop in range(5):
    NumbersFromInput = int(input('Type a number: '))
    if Loop == 0 or NumbersFromInput > NumbersList[-1]:
        NumbersList.append(NumbersFromInput)
    else:
        Position = 0
        while Position < len(NumbersList):
            if NumbersFromInput < NumbersList[Position]:
                NumbersList.insert(Position, NumbersFromInput)
                break
            Position += 1
print('\n' + '-=' * 40)
print(f'The sequence of values entered was {NumbersList}')