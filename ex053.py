FraseUsuario = input('Digite uma frase: ').strip().upper()
PalavrasDivididas = FraseUsuario.split()
PalavrasJuntas = ''.join(PalavrasDivididas)
FraseInversa = PalavrasJuntas[::-1]

print(f'\nA frase digitada foi \033[43;1;30m{PalavrasJuntas}\033[0;0m e o inverso dela é \033[43;1;30m{FraseInversa}\033[0;0m.')

if PalavrasJuntas == FraseInversa:
	print('\n\033[1;32mA FRASE ACIMA É UM PALÍNDROMO\033[0m')
	
else:
	print('\n\033[1;31mA FRASE ACIMA NÃO É UM PALÍNDROMO\033[0m')