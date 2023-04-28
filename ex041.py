# Exercicio 041
from datetime import date

AtletaIdade = int(input('Digite o ano de nascimento do atleta: '))
AnoAtual = date.today().year
Idade = AnoAtual - AtletaIdade

print(f'\nO atleta em questão tem {Idade} anos.\n')

if Idade <= 9:
	print('CLASSIFICAÇÃO: MIRIM')
	
elif Idade <= 14:
	print('CLASSIFICAÇÃO: INFANTIL')
	
elif Idade <= 19:
	print('CLASSIFICAÇÃO: JUNIOR')
	
elif Idade <= 25:
	print('CLASSIFICAÇÃO: SENIOR')
	
else:
	print('CLASSIFICAÇÃO: MASTER')