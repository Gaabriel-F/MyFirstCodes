# Exercicio 039

from datetime import date

AnoAtual = date.today().year
Nasc = int(input('Digite o seu ano de nascimento: '))
Idade = AnoAtual - Nasc
print(f'\nQuem nasceu em {Nasc} tem {Idade} anos em {AnoAtual}')

if Idade == 18:
	print('Se aliste IMEDIATAMENTE!!!')
	
elif Idade < 18:
	saldo = 18 - Idade
	print(f'Ainda faltam {saldo} anos para você se alistar')

elif Idade > 18:
	saldo = Idade - 18
	print(f'Você deveria ter se alistado há {saldo} anos.')