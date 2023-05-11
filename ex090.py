# Exercise 090 - Learning about Dictionary.

# Variable that stores the student's data.
studentGrade = {}

# Adding keys along with values to the named dictionary 'studentGrade'.
studentGrade['Name'] = str(input("Name: "))
studentGrade['Average'] = float(input(f"What was {studentGrade['Name']}`s avarage?: "))

# Final part.
print('-='*25)

# Verify if the student is aproved, in recovery or reproved.
if studentGrade['Average'] >= 7.0:
    print('STATUS: \033[1;32mAPROVED\033[0;0m')

elif studentGrade['Average'] >= 5.0 and studentGrade['Average'] < 7.0:
    print('STATUS: \033[1;33mIN RECOVERY\033[0;0m')

else:
    print('STATUS: \033[1;31mREPROVED\033[0;0m')
