# Define a player sketch and show the values to the user.

def PlayerProfile(player='<unknown>', goals=0):
    print(f'{player} has scored {goals} goals in the championship')

# Main program.
player_name = input('Type a player\'s name: ')
while True:
    if player_name.isalpha():
        break
    else:
         player_name = input('Type a \033[1;31mVALID\033[0;0m player\'s name: ')
         continue

# Passing the conditions to the function "PlayerProfile".

# Checking if the player's name is empty or not.
if player_name != '':
    player_goals = input(f'Type the goals that {player_name} scored: ')
else:
    player_goals = input('Type the goals that <unknown> scored: ')

# Checking the goals.
if player_goals.isnumeric():
    player_goals = int(player_goals)
else:
    player_goals = 0

if player_name == '':
    PlayerProfile(goals=player_goals)
else:
    PlayerProfile(player_name, player_goals)
