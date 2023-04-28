# Exercicio 029

Veloc = float(input('Qual a velocidade atual do carro em km/h: '))

VeloCalculo = (Veloc - 80) * 7

if Veloc <= 80:
	print('\n\033[0;33mTenha um bom dia e dirija com cautela!\033[0;0m')
	
if Veloc >= 80:
	print(f'\n\033[1;31mVOCÊ FOI MULTADO!!\033[0;0m Você excedeu o limite de \033[1;31m80Km/h\033[0;0m! O valor total da multa é de R$\033[0;32m{VeloCalculo:.2f}\033[0;0m')