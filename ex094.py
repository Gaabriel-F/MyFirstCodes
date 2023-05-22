# List that will keep a copy of the dictionaries created.
listForPersonData = []
ageSum = 0

while True:
    print('-' * 40, '\n')
    print(' ' * 8 + 'REGISTER A PERSON')
    print('\n' + '-' * 40)
    print()
    
    # Create a new dictionary for each person.
    personData = {"Name": '', "Age": []}
    personData["Name"] = str(input("Name: "))

    # Loop using try-except to validate the person's age.
    while True:
        try:
            Age = int(input("Age: "))
            personData["Age"].append(Age)
            break
        except ValueError:
            pass
    ageSum += Age
    
    # Create a key in the dictionary for gender, with validation.
    personData["Gender"] = input("Gender [M/F]: ").upper().strip()[0]
    while personData["Gender"] not in ['M', 'F']:
        personData["Gender"] = str(input('Gender [M/F]: ')).upper().strip()[0]
        
    # Copying the person data to the list.
    listForPersonData.append(personData.copy())
    personData.clear()
        
    # Separte the registration from the stop condition.
    print('\n' + '-' * 40)
    
    # Stop contition.
    Continuation_Option = str(input('\nDo you want to continue? [Y/N]: ')).upper().strip()[0]
    print()
    
    # Validate the stop condition.
    if Continuation_Option in 'YN':
        if Continuation_Option == 'Y':
            continue
        if Continuation_Option == 'N':
            break
    else:
        while Continuation_Option not in 'YN':
            Continuation_Option = str(input('\nDo you want to continue? [Y/N]: ')).upper().strip()[0]
            print()
        if Continuation_Option == 'N':
            break

# Calculate the average age.
averageOfAge = ageSum / len(listForPersonData)

#Final results.
print(f'''A) {len(listForPersonData)} people were registered.
B) The average age is {averageOfAge:.1f}''')
print(f'C) The female(s) registred was: ',end='')

# For each dictionary in our list that stores the data, we check if the person has the key "Gender" with the value "F".
for person in listForPersonData:
    if person["Gender"] == 'F':
        print(person["Name"], end=' ')
print()

# Loop "for" with another "for" loop inside to check if the key "Age" in the personData dictionary is above the average.
print('D) People list whose age is above the average: ')

# Iterate through each dictionary created for each person.
for person in listForPersonData:

    # Create another "for" loop to check if the person's age is above the average.
    for age in person['Age']:

        # Perform the validation.
        if age >= averageOfAge:
            print(' ')
            for key, value in person.items():
                print(f'{key} = {value} ', end='')
