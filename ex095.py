# Create a function to show a line.
def showLine():
    print()
    print('-='*45)
    print()

# Create a list to store the copy of the dictionary 'playerPerformance'.
playersList = list()

# Create a dictionary to store name, played matches, and goals.
playerPerformance = {}

#
while True:
    
    # Adding the player's name to the dictionary.
    playerPerformance["Name"] = input('Player`s name: ').title()
    
    # Create a variable to store the quantity of matches.
    playedMatches = int(input(f'How many matches {playerPerformance["Name"]} played?: '))
    print()
    
    # Create a dictionary for goals in matches inside the our first dict named playerPerformance
    playerPerformance["goalsInMatches"] = list()
    
    # Loop created to store the quantity of goals in each match.
    for matches in range(1, playedMatches+1):
    
        # Asking for the quantity of goals the player scored and assigning the quantity of goals to the key, named by "goalsInMatches", created to store the goals in the match.
        playerPerformance["goalsInMatches"].append(int(input(f'Number of goals in match {matches}: ')))
        
        # Calculate the total number of goals.
        playerPerformance["goalsTotal"] = sum(playerPerformance["goalsInMatches"])
        
        
    # Copy the data from the dictionary.
    playersList.append(playerPerformance.copy())
    playerPerformance.clear()
    
    # Stop condition with another loop.
    while True:
        print()
        Continuation = str(input('Do you want to continue? [Y/N]: ')).upper().strip()[0]
        if Continuation in ['Y', 'N']:
            print()
            break
    if Continuation == 'N':
        break

# Show a line to separate sections.
showLine()
print(f'{"No.":<6}{"PLAYERS":>4} {"GOALS":>12} {"TOTAL GOALS":>19}')
print()

#Loop to display the player's performance.
for pos, players in enumerate(playersList):
    print(f'{pos:<6} {players["Name"]:<13} {players["goalsInMatches"]}{players["goalsTotal"]:>11}')

# Show a line to separate sections.
showLine()

# Loop to ask wich player's statics the user would like to see.
while True:
    searchPlayer = input("Which player's statistics would you like to see? ([S] to stop): ").strip()[0]
    
    # Stop condition.
    if searchPlayer.upper() == 'S':
        break
    print()
    
    # Checking if the input is valid.
    if int(searchPlayer) >= len(playersList):
        print(f'\033[1;31mError\033[0;0m... there is no player with the number {int(searchPlayer)}\n')
    else:
        showLine()
        
        # Showing the player's statistics.
        print(f'{playersList[int(searchPlayer)]["Name"]}\'s statistics:\n')
        
        # Display the player's name and the number of matches played.
        print(f'{playersList[int(searchPlayer)]["Name"]} played {playedMatches} matches.')
        print()
        
        # Loop to display the goals scored in each match.
        for match, goals in enumerate(playersList[int(searchPlayer)]["goalsInMatches"]):
            print(f'In the {match+1}° match, {playersList[int(searchPlayer)]["Name"]} scored {goals} goals.')
        
        # Show a line to separate sections.
        showLine()
