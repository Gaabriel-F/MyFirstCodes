#Temporary list to store data.
temporaryList = []

#This will be the main list that will receive the data from the temporaryList.
mainList = []
biggestWeight = lowestWeight = 0
while True:
    
    #Code block for registering people. - Part 1
    temporaryList.append(str(input("Name: ")))
    temporaryList.append(float(input("Weight: ")))
    
    #Code block for defining values for: Heaviest people and lightest people.
    if len(mainList) == 0:
        biggestWeight = lowestWeight = temporaryList[1]
    else:
        if temporaryList[1] > biggestWeight:
            biggestWeight = temporaryList[1]
            
        if temporaryList[1] < lowestWeight:
            lowestWeight = temporaryList[1]
        
    mainList.append(temporaryList[:])
    temporaryList.clear()
        
    
    #Stop condition with validation.
    Continuation = input("Do want to continue? [Y/N]: ").strip().lower()[0]
    if Continuation == "y":
        continue
    else:
        while Continuation not in ["y", "n"]:
             Continuation = input("Do want to continue? [Y/N]: ").strip().lower()[0]
    if Continuation == "n":
        break
        
#Final results.
print("\n", "-="*50)
print(f"We have {len(mainList)} people registred.")
print(f"The heaviest weight listed is {biggestWeight:.2f}lbs. Weight of", end=' ')
for heaviestPerson in mainList:
    if heaviestPerson[1] == biggestWeight:
        print(f"[{heaviestPerson[0]}]", end='')
print()
print(f"The lightest weight listed is {lowestWeight:.2f}lbs. Weight of", end=' ')
for lightestPerson in mainList:
    if lightestPerson[1] == lowestWeight:
        print(f"[{lightestPerson[0]}]", end='')
print()