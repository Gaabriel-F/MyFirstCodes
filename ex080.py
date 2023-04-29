NumbersList = []
for Loop in range(5):
    NumbersFromInput = int(input('Type a number: '))
    if Loop == 0 or NumbersFromInput > NumbersList[-1]:
        NumbersList.append(NumbersFromInput)
        print('value added at the last position of the list')
        
    else:
        Position = 0
        while Position < len(NumbersList):
            if NumbersFromInput <= NumbersList[Position]:
                NumbersList.insert(Position, NumbersFromInput)
                print(f'Value added at the {Position} position of the list')
                break
            Position += 1

print('\n' + '-=' * 40)
print(f'The sequence of values entered was {NumbersList}')
