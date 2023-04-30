ValuesList = []
NumbersEven = []
NumbersOdd = []
while True:
    ValuesList.append(int(input('Type a value: ')))

    # Ask for continuation. 
    Continuation = input('Do want to continue? Y/N: ').strip().lower()[0]

    # Validation of the continuation question.
    while Continuation not in ['y', 'n']:
        Continuation = input('Do want to continue? Y/N: ').strip().lower()[0]
    if Continuation == 'y':
        continue
    if Continuation == 'n':
        break

# Separating Odd and Even from the list
for Index, EvenOrOdd in enumerate(ValuesList):
    if EvenOrOdd % 2 == 0:
        NumbersEven.append(EvenOrOdd)
    else:
        NumbersOdd.append(EvenOrOdd)

# Final results
print('\n' + '-=-'*30)
print(f'\nThe full list is {ValuesList}')
print(f'The list of even numbers is {sorted(NumbersEven)}')
print(f'The list of odd numbers is {sorted(NumbersOdd)}')
