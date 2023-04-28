# Exercicio 024

Cdd = str(input('Digite o nome da cidade em que você nasceu: ')).strip().upper()

# ajustes
tf = 'SANTO' in Cdd


if tf == True:
	print(f'\nA cidade citada é {Cdd.title()} e ela tem "Santo" no nome.')

else:
		print(f'\nA cidade citada é {Cdd.title()} e ela não tem "Santo" no nome.')