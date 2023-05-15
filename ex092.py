from datetime import datetime as dT

# Create a dictionary for person data.
personData = dict()

# Adding a person's name to the dictionary.
personData["Name"] = str(input('Name: '))

# Creating a variable called 'Birth' to later use it when calculating age and retirement.
Birth = int(input('Year of birth: '))

# Calculating the person's age.
personData["Age "] = dT.now().year - Birth

# Ask if the person has a work card.
personData["WCSN"] = int(input('Work Card Serial Number ([0] I don`t have it): '))

# The person has a Work Card so we can ask about the Year of hire and Salary, so we can calculate the Retirement.
if personData["WCSN"] != 0:
    personData["Hired"] = int(input('Year of hire: '))
    personData["Salary"] = float(input('Salary: USD '))
    personData["Retirement"] = personData["Age "] + ((personData["Hired"] + 35) - dT.now().year)
    
# Displaying the results
print()
print('-='*30)
print()
for Keys, Values in personData.items():
    print(f'• {Keys}:  {Values}')
print()
print('-='*30)
