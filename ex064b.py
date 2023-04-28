# Exercicio 064
import itertools
user_input = total_sum = counter = 0
user_input = int(input('Digite um número [999 para parar]: '))
for t in itertools.count():
    counter += 1
    total_sum += user_input
    user_input = int(input('Digite um número [999 para parar]: '))
    if user_input == 999:
        break
print(f'\nVocê digitou {counter} números e a soma entre eles é {total_sum}')