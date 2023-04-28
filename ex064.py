# Exercicio 064
Number_User = Sum = Counter = 0
Number_User = int(input('Digite um número [999 para parar]: '))
while Number_User != 999:
    Counter += 1
    Sum += Number_User
    Number_User = int(input('Digite um número [999 para parar]: '))
print(f'\nVocê digitou {Counter} números e a soma entre eles é {Sum}')