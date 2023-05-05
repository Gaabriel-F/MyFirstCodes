'''This code will run by asking some values
to the user and in the final of the code will
appear the results of: Value 5 is in the list?
List in order, quantity of elements typed.'''

NumbersList = []

while True:
    ValuesInput = int(input('Type a value: '))
    NumbersList.append(ValuesInput)

    # Ask to user if he wants to continue typing numbers.
    Continuation = input('Do you want to continue? Y/N: ').strip().lower()[0]
    while Continuation not in ['y', 'n']:
        Continuation = input('Do you want to continue? Y/N: ').strip().lower()[0]
    if Continuation == 's':
        continue
    if Continuation == 'n':
        break

# Final results.
print('-='*40)
print(f'''You typed {len(NumbersList)} elements.
The descending order of the list is {sorted(NumbersList, reverse=True)}''')
print('The value 5 is in the list' if 5 in NumbersList else 'the value 5 doesn`t appear in the list')
