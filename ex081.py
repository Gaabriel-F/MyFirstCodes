NumbersList = []
CounterNumbers = 0
while True:
    ValuesInput = int(input('Type a value: '))
    NumbersList.append(ValuesInput)
    CounterNumbers += 1

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
print(f'''You typed {CounterNumbers} elements.
The descending order of the list is {sorted(NumbersList, reverse=True)}''')
if 5 in NumbersList:
    print('The value 5 is in the list')
else:
    print('the value 5 doesn`t appear in the list')
