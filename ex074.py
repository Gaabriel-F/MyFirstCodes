#Exercicio 074
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram {numeros}')
print(f'O maior numero sorteado foi: {max(numeros)}')
print(f'O menor número sorteado foi: {min(numeros)}')