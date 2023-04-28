# Exercicio 037
from time import sleep
import emoji

while True:#loop para verificar se o input é ou nao numero
    ValorConversao = input('\033[1;35mDigite um valor para conversão\033[1;0m: \033[1;33m')
    print('\033[0m')
    if ValorConversao.isdigit():
        ValorConversao = int(ValorConversao)
        print()
        break
    else:
        print(emoji.emojize('\n\n\033[1;31mDigite apenas números inteiros\033[0;0m!! :warning: \n\n'))
        continue
        
while True:#loop de repeticao para a escolha de opcao
        	
        	OpcoesConversao = input('\033[4;32mEscolha uma das opções abaixo\033[0;0m para converter o número que você digitou\n\n\n\033[1;36m[1] Binário\033[0;0m \033[1;35m[2] Octal\033[0;0m \033[1;34m[3] Hexadecimal\033[0;0m\n\n> ')
        	
        	print('')
        	
        	if OpcoesConversao.isdigit():#verifica se é ou não numero, caso não seja o else entra em ação e repete até o loop se encerrar
        		Op = int(OpcoesConversao)
        		
        		if Op == 1:
        			valor = int(ValorConversao)
        			tt = bin(valor)
        			print(f'\033[1;33mConvertendo\033[0;0m...', end='\r', flush=True)
        			sleep(2)
        			print(' '*len('Convertendo...'), end='\r', flush=True)
        			print(f'\033[1;33m{tt[2:]}\033[0;0m')
        			break
        		
        		if Op == 2:
        			valor = int(ValorConversao)
        			tt = oct(valor)
        			print(f'\033[1;33mConvertendo\033[0;0m...', end='\r', flush=True)
        			sleep(2)
        			print(' '*len('Convertendo...'), end='\r', flush=True)
        			print(f'\033[1;33m{tt[2:]}\033[0;0m')
        			break
        		
        		if Op == 3:
        			valor = int(ValorConversao)
        			tt = hex(valor)
        			print(f'\033[1;33mConvertendo\033[0;0m...', end='\r', flush=True)
        			sleep(2)
        			print(' '*len('Convertendo...'), end='\r', flush=True)
        			print(f'\033[1;33m{tt[2:]}\033[0;0m')
        			break
        		
        	else:#mensagem de erro basica com clean do console
        		print(emoji.emojize('\n\033[1;31mOpção invalida\033[1;0m. Tente novamente :warning:\n'))
        		sleep(3)
        		print("\x1b[2J\x1b[1;1H")
        		continue