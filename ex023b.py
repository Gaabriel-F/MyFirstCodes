# Começo do planejamento do code

TentativasNumero = 0
Limite = 3

# Primeira parte - construção da estrutura de loop para a condição necessária 

while True:
    Numeros = input('Digite um número inteiro de\033[1;31;40m 1\033[1;0;0m a \033[1;31;40m9999\033[1;0;0m: ')

    try:
        Numeros = int(Numeros)
        
    except ValueError:
        print("\n\033[1;31;40mErro... \033[1;31;00mVocê colocou letras ou algum outro caractere que não é um numero. Por favor, digite um número.\n")
        TentativasNumero += 1
        
        if TentativasNumero == Limite:
            print("\nVocê \033[1;33mexcedeu\033[0;0m o número de tentativas permitidas. Por favor, reinicie e digite novamente um número correto!\n")
            TentativasNumero = 0
            
    else:
        if 1 <= Numeros <= 9999:
            break
            
        else:
            print('\nValor inválido, insira um número inteiro entre\033[1;31;40m 1\033[0;0m e \033[1;31;40m9999\033[0;0m.\n')
            TentativasNumero += 1
            
            if TentativasNumero == Limite:
                print("\nVocê \033[1;33mexcedeu\033[0;0m o número de tentativas permitidas. Por favor, reinicie e digite novamente um número correto!\n")
                TentativasNumero = 0
                continue

# Resultados que aparecerão ao usuario

u = Numeros // 1 % 10
d = Numeros // 10 % 10
c = Numeros // 100 % 10
m = Numeros // 1000 % 10


if u == 0:
	print('\n\033[1;31;40mNão há\033[0;0m unidade\n')
	
else:
	print(f'\nA unidade é \033[1;31;40m{u}\n\033[0;0m')
	
if d == 0:
	print('\n\033[1;31;40mNão há\033[0;0m dezena\n')
	
else:
	print(f'\nA dezena é \033[1;31;40m{d}\n\033[0;0m')
	
if c == 0:
	print('\n\033[1;31;40mNão há\033[0;0m centena\n')
	
else:
	print(f'\nA centena é \033[1;31;40m{c}\n\033[0;0m')
	
if m == 0:
	print('\n\033[1;31;40mNão há\033[0;0m milhar\n')
	
else:
	print(f'\nA milhar é \033[1;31;40m{m}\n\033[0;0m')