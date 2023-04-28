# Primeira parte, importação e definição do limite de tentativas.


TentativasNumero = 0
Limite = 3
from sty import fg, rs

# Segunda parte - Estrutura do limite de tentativas, aplicação do input ao usuário e mensagens de erro.

while True:
    Numeros = input('Digite um número inteiro de' + fg.red + ' 1' + fg.rs + ' a ' + fg.red + '9999' + fg.rs + ': ')

    try:
        Numeros = int(Numeros)
        
    except ValueError:
        print("\n" + fg.red + "Erro..." + fg.rs + " Você colocou letras ou algum outro caractere que não é um numero. Por favor digite um número.\n")
        TentativasNumero += 1
        
        if TentativasNumero == Limite:
            print("\nVocê" + fg.red + " excedeu" + fg.rs + " o número de tentativas permitidas. Por favor, reinicie e digite novamente um número correto!\n")
            TentativasNumero = 0
            
    else:
        if 1 <= Numeros <= 9999:
            break
            
        else:
            print("\nValor inválido, insira um número inteiro entre" + fg.red + ' 1' + fg.rs + ' e ' + fg.red + '9999' + fg.rs + ".\n")
            TentativasNumero += 1
            
            if TentativasNumero == Limite:
                print("\nVocê" + fg.red + " excedeu" + fg.rs + " o número de tentativas permitidas. Por favor, reinicie e digite novamente um número correto!\n")
                TentativasNumero = 0
                continue

# Terceira parte - Ajuste na posição dos números e mensagem que ira aparecer ao usuário final.

Numeros = str(Numeros + 10000)

if len(Numeros) >= 4:
    print('\nA Unidade é ' + fg.red + f' {Numeros[4]}' + fg.rs)
else:
    print("\nNão há unidade\n")

if len(Numeros) >= 3:
    print('\nA Dezena  é ' + fg.red + f' {Numeros[3]}' + fg.rs)
else:
    print("\nNão há dezena\n")

if len(Numeros) >= 2:
    print('\nA Centena é ' + fg.red + f' {Numeros[2]}' + fg.rs)
else:
    print("\nNão há centena\n")

if len(Numeros) >= 1:
    print('\nA Milhar  é' + fg.red + f'  {Numeros[1]}\n' + fg.rs)
else:
    print("\nNão há milhar\n")
