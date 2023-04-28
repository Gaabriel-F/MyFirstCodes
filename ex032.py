#Exercicio 032

User_Year_input = int(input('Digite um ano qualquer: '))

if User_Year_input % 100 != 0 and User_Year_input % 4 == 0 or User_Year_input % 400 == 0:
    print('\nO ano digitado é um ano bissexto!!')
else:
    print('\nNão é um ano bissexto.')
