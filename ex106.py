# Program to show the interactive help list to the user.
comando = ''

while True:

    #Showing the "menu" of the program.
    print('=' * 35, '\n')

    titulo = print('\033[3;33;1m     HELP SOFTWARE - PYHELP\033[m', '\n')

    print('=' * 35)

    #Asking the function or library to the user.
    comando = str(input('Function or Library ----> '))

    #Stop condition.
    if comando == 'FIM':
        break

    #Continue the loop.
    else:
        help(comando)
        print('\n')
