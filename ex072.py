#Exercicio 072

NumeroExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    print('')
    User_input = input('Digite um número entre 0 e 20: ')
    if User_input.isnumeric() and int(User_input) in range(21):
        User_input = int(User_input)
        pass
    elif User_input.isalpha() or User_input.isalnum():
        print('\n\033[1;31mErro\033[0;0m... Digite um número entre 0 e 20\n')
        continue
    print(f'\nVocê digitou {NumeroExtenso[User_input]}\n')
    
    Continuation_Ask = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while Continuation_Ask not in ['S', 'N']:
        Continuation_Ask = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if Continuation_Ask == 'N':
        break