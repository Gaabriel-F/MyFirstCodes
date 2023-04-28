# Exercicio 052

print('~=' * 25)
print('\n        \033[1;42mValidador de números primos\033[0m\n')
print('~=' * 25)

count = 0 #Valor que determinará quantas vezes o número foi dividido
NumeroUsuario = int(input('\nDigite um número: ')) # Aqui é pedido a entrada do usuário para que mais tarde seja usada no cálculo de validação dos números primos.
print()

for C in range(1, NumeroUsuario + 1):
	if NumeroUsuario % C == 0: # Se a divisão tiver resto 0 quer dizer que este número não é primo e marcará os numeros de verde e irá contar quantas vezes foi dividido, com o else acontecera a mesma coisa exceto que só será contado 2 vezes
		print(f'\033[1;32m', end = ' ')# print para colorir números divisores
		count +=  1 
	else:
		print(f'\033[1;31m', end = ' ') # mesma função do print acima
	print(C, '\033[0m', end = ' ') #print para mostrar os números
	
print(f'\n\n\033[1;37mO NÚMERO {NumeroUsuario} FOI DIVISÍVEL {count} VEZES.\033[0m')

if count == 2: # aqui é o resultado da contagem ser 2 que nos determinará que com uma contagem 2 é determinado como primo, sendo 3 ou mais é determinado como não primo
	print('\033[1;37mClassificação \033[1;32mPRIMO\033[0m')
	
elif count == 1:
	print('\033[1;37mClassificação \033[1;32mPRIMO\033[0m')
	
else:
	print('\033[1;37mClassificação \033[1;31mNÃO PRIMO\033[0m')