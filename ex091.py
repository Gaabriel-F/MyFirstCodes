# Create the dictionary and call the random
from random import randint
from operator import itemgetter
from time import sleep
PlayersDict = {'Player1': randint(1, 6), 'Player2': randint(1, 6), 'Player3': randint(1, 6), 'Player4': randint(1, 6)}
Ranking = dict()

# Displaying the sorted numbers.
print('-='*35)
print()
sorted(PlayersDict.values(), reverse=True)
for Player, Items in PlayersDict.items():
    print(f'{Player} rolled a {Items} on the dice')
    sleep(1.3)
    
# Setting the display for ranking partSetting the display to show the parts in order of ranking
print()
print('-='*35)
print()
print(f'{"RANKING":^20}')
print()
print(f'{"No.":<6}{"PLAYERS":>4} {"RESULT":>10}')
print()

# Ordering the Ranking Dictionary in ascending order and displaying the results.
Ranking = sorted(PlayersDict.items(), key=itemgetter(1), reverse=True)
for Rank, Player in enumerate(Ranking):
    sleep(1.4)
    print(f'{Rank+1:<6}{Player[0]:>4}{Player[1]:>10}')
sleep(0.85)
print('\n\n' +  '-='*35)