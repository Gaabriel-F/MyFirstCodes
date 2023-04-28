# Exercicio 059

from time import sleep

#Será usado este loop validação dos números digitados pelo usuário.
while True:
	#Usaremos a função try e except para tratar possíveis erros de digitação e uso de opções inválidas.
	try:
		NumeroDigitado1 = int(input('Digite um valor: '))
		NumeroDigitado2 = int(input('Digite outro valor: '))
		break
	except ValueError:
		print('\n\033[1;31mErro\033[0;0m... Digite um número inteiro valido!!\n')
sleep(1)
print()
EncerramentoMenu = False

#Aqui daremos início ao menu.
while not EncerramentoMenu:
	print("~="*25, '''\nEscolha a opção desejada.

[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS VALORES
[5] SAIR
''' + "~="*25)
	
	#Tratando erro de opção inválida.
	try:
		EntradaUsuario = int(input('\n\n----> '))
	except ValueError:
		print('\n' + "~="*25 + '\n\n\033[1;31mOpção inválida\033[0;0m... Tente novamente!\n')
		sleep(1.3)
		continue
		
	sleep(1.5)
	
	#A cada opção escolhidas tais como: 1, 2, 3, 4 e 5 o programa executará uma ação diferente como soma, mutiplicação e afins...
	if EntradaUsuario == 1:
		#Somando valores + resultado.
		Soma = int(NumeroDigitado1) + int(NumeroDigitado2)
		print('\n' + "~="*25 + f'\n\nA soma entre {NumeroDigitado1} e {NumeroDigitado2} resulta em: {Soma}\n')
		sleep(1.3)
		
	if EntradaUsuario == 2:
		#Multiplicando valores digitados + resultado.
		Multiplicar = int(NumeroDigitado1) * int(NumeroDigitado2)
		print('\n' + "~="*25 + f'\n\nA multiplicação entre {NumeroDigitado1} e {NumeroDigitado2} resulta em: {Multiplicar}\n')
		sleep(1.3)
	
	if EntradaUsuario == 3:
		#Verificando valores maiores, menores e iguais + resultados.
		if int(NumeroDigitado1) > int(NumeroDigitado2):
			print('\n' + "~="*25 + f'\n\nO primeiro valor ({NumeroDigitado1}) é MAIOR.\n')
		if int(NumeroDigitado1) < int(NumeroDigitado2):
			print('\n' + "~="*25 + f'\n\nO segundo valor ({NumeroDigitado2}) é MAIOR.\n')
		elif int(NumeroDigitado1) == int(NumeroDigitado2):
			print('\n' + "~="*25 + f'\n\nAmbos os valores são iguais, não há maior e menor.\n')
		sleep(1.3)
		
	if EntradaUsuario == 4:
		#Novo input do usário para outros valores
		sleep(1.3)
		print()
		#na linha 67 será usado o loop while True para a validação das entradas feitas pelo usuário de novos valores.
		while True:
		   	NumeroDigitado1 = input('Digite um valor: ')
		   	if NumeroDigitado1.isalpha():
		   	    print('\n\033[1;31mErro\033[0;0m... Tente novamente...\n')
		   	    continue
		   	NumeroDigitado2 = input('Digite outro valor: ')
		   	if NumeroDigitado2.isalpha():
		   	    print('\n\033[1;31mErro\033[0;0m... Tente novamente...\n')
		   	    continue
		   	if NumeroDigitado1.isnumeric() and NumeroDigitado2.isnumeric():
		   	    break
		print()
		continue
	
	# Opção para parada.
	if EntradaUsuario == 5:
		sleep(1.8)
		print('\n\033[1;34mFinalizando...\033[0;0m')
		sleep(1.8)
		EncerramentoMenu = True

#Print de encerramento.
print('\n\033[44;1;30mFim do programa!\033[0;0m Tenha um bom dia.')