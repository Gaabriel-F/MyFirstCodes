#EntradaUsuario = int(input("Digite um número para ver o seu fatorial: "))
#cont = 1
#for Fatoracao in range(1, EntradaUsuario):
	#EntradaUsuario *= Fatoracao
	#cont += 1
#print(f'\nO fatorial de {cont} resulta em {EntradaUsuario}')

from math import factorial
EntradaUsuario = int(input("Digite um número para ver o seu fatorial: "))
Contador = EntradaUsuario
Fatorial = factorial(EntradaUsuario)
print(f'\nCalculando {EntradaUsuario}! = ', end='')
while Contador > 0:
	print(f'{Contador}', end=' ')
	Contador -= 1
	print('x ' if Contador > 0 else f'= {Fatorial}\n', end='')
