# Exercicio 038

ValorUm = int(input('Digite um valor: '))
ValorTwo = int(input('Digite um segundo valor: '))

if ValorUm > ValorTwo:
	print('\nO \033[4;32mPrimeiro valor\033[0;0m é \033[4;32mmaior\033[0;0m!')
	
elif ValorUm < ValorTwo:
	print('\nO \033[4;31mSegundo valor\033[0;0m é \033[4;31mmaior\033[0;0m!')
	
elif ValorUm == ValorTwo:
	print('\nXiii... \033[1;36mOs dois valores são iguais\033[0;0m')
