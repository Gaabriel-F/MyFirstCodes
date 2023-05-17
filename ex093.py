# Create a function to show a line.
def showLine():
    print()
    print('-='*45)
    print()

# Create a dictionary to store name, played matches, and goals.
playerPerformance = {}

# Adding the player's name to the dictionary.
playerPerformance["Name"] = input('Player`s name: ')

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
goalsTotal = sum(playerPerformance["goalsInMatches"])  # Total number of goals in all matches

# Show a line to separate sections.
showLine()

# Display player's name, goals in each match, and total goals.
print(f'{playerPerformance["Name"]} - {"GOALS"} {playerPerformance["goalsInMatches"]} - {"GOALS TOTAL"} {goalsTotal}')

# Show a line to separate sections.
showLine()

# Display the player's name and the number of matches played.
print(f'{playerPerformance["Name"]} played {playedMatches} matches.')
print()

# Loop to display the goals scored in each match.
for match, goals in enumerate(playerPerformance["goalsInMatches"]):
    print(f'In the {match+1}° match, {playerPerformance["Name"]} scored {goals} goals.')

# Show a line to separate sections.
showLine()
