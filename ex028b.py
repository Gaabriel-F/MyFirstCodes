# Parte de importações e desc.

import random, time, emoji

MaquinaParte = random.randrange(0, 6)

print('\n\033[1;33mBem-vindo! \033[0;0meste arquivo python é um joguinho de adivinhação feito por \033[1;36mG.Felix!\033[0;0m\n')

# Parte 2: Definição do input e ajustes para possiveis erros

while True:
    PessoaParte = input('~-' * 38 + '\n\n\033[1;31mVamos dar inicio ao jogo!\033[0;0m\n\nEscolha \033[1;31muma\033[0;0m das opções abaixo para o seu palpite e tente adivinhar em que número eu estou pensando...\n\n\033[1;36m[0]\033[0;0m \033[1;35m[1]\033[0;0m \033[1;34m[2]\033[0;0m \033[1;33m[3]\033[0;0m \033[1;32m[4]\033[0;0m \033[1;30m[5]\033[0;0m\n\n' + '~-' * 38 + '\n\n\033[1;32m---> \033[0;0m').strip()
    
    if PessoaParte.isnumeric() and int(PessoaParte) in range(6):
        
        break
        
    else:
        time.sleep(2)
        print('\n\033[1;33mAlgo deu errado. Analisando...\033[0;0m')
        time.sleep(1.6)
        print('\n\033[1;31mEntrada inválida\033[0;0m! Digite apenas os números entre \033[1;31m0\033[0;0m e \033[1;31m5.\033[0;0m')
        time.sleep(2.4)
        
# Limpa o console após a mensagem de erro
        
        print('\033[H\033[J')

# Parte para resultados

print(emoji.emojize('\n\033[1;33mVamos ver se seu palpite está correto...\033[0;0m :eyes: \n'))

time.sleep(2)

if int(PessoaParte) == MaquinaParte:
    print(emoji.emojize('Você \033[1;32macertou\033[0;0m!! Dessa vez você me pegou... :cowboy_hat_face: '))
else:
    print(f'O número que eu escolhi foi \033[1;41m {MaquinaParte} \033[0;0m, infelizmente, \033[1;31mvocê não acertou\033[1;0m... Quem sabe na próxima? rs')
