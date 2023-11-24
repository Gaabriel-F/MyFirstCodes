# Criar uma validação de entrada do usuário para números inteiros.

def EntradaUsuario(frase):
    msg = input(frase) 
    
    while True:


        if msg.isnumeric():
            valor = int(msg)
            break


        else:
            msg = input('VOCÊ \033[1;31mDIGITOU UM NÚMERO INVÁLIDO\033[0;0m, TENTE NOVAMENTE: ')
            continue

    return valor


# Main Program.
n = EntradaUsuario('Digite um número: ')
print(f'\nO NÚMERO DIGITADO FOI \033[1;32m{n}\033[0;0m!')