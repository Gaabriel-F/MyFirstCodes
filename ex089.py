academicRecord = []
while True:
    name = str(input("Name: "))
    grade1 = float(input("Grade 1: "))
    grade2 = float(input("Grade 2: "))
    
    # Ask for stop condition + validating the response.
    Continuation = input("Do you want to continue? [Y/N]: ").strip().lower()[0]
    while Continuation not in ['y', 'n']:
        Continuation = input("Do you want to continue? [Y/N]: ").strip().lower()[0]
    academicAverage = (grade1 + grade2) / 2
    academicRecord.append([name, [grade1, grade2], academicAverage])
    if Continuation == 'y':
        continue
    if Continuation == 'n':
        break

# Display the student`s records
print('-='*25)
print(f'{"No.":<5}{" NAME":<11}{"AVARAGE":>16}')
print('-'*35)
for Index, Student in enumerate(academicRecord):
    print(f'{ Index:<6}{Student[0]:<10}{Student[2]:>15.1f}')

#Loop to ask if the user wants to see the grade of any students
while True:
    print('-'*35)
    numStudent = input("Do you want to see the grade of any student? [999 to stop]: ").strip()

    #The validation checks whether the numStudents variable is a stop condition. If it is not, we verify whether
    # it is numerical and within the range of the students' records.
    if numStudent.isnumeric() and int(numStudent) == 999:
        break
    if numStudent.isnumeric() and int(numStudent) in range(Index+1):
        pass
    else:
        print('-'*35)
        print("\nStudent \033[1;31mnot found\033[0;0m. Please \033[4;32menter only numbers\033[0;0m! The valid numbers are the ones listed in \033[1;44mNo.\033[0;0m\n")
        continue

    # After passing the validations above, the code below will display the student's name and their respective grades and restart the loop.
    if int(numStudent) <= len(academicRecord) - 1:
        print('-'*35)
        print(f'\nthe {academicRecord[int(numStudent)][0]}`s grade is {academicRecord[int(numStudent)][1]}\n')
