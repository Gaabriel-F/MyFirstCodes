from emoji import emojize
from time import sleep
from random import choice

print('\033[1;35m===Bem-vindo ao minigame "JOKENPO"!===\033[m')
print('')

while True:
    Jogador = str(input('\n\033[1;33mPedra, Papel ou Tesoura?\033[0;0m: ')).upper().strip()
    opcoes = ('PAPEL', 'PEDRA', 'TESOURA')
    BotPart = choice(['PAPEL','PEDRA','TESOURA'])

    while Jogador not in opcoes:
        Jogador = input("Opção inválida. Escolha \033[1;33mPedra, Papel ou Tesoura\033[0;0m: ").upper().strip()
    sleep(1)
    print(emojize('\n\033[1;33mJO'))
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!\n')
    sleep(0.5)

    # empate
    if Jogador == BotPart:
        print(emojize('\033[1;34mEmpate! (Eu escolhi {})\033[0;0m'.format(BotPart.title())))

    # você ganha
    elif Jogador == 'PAPEL' and BotPart == 'PEDRA':
        print(emojize('\033[1;36mVocê Ganhou! (Eu escolhi Pedra :moai:))\033[0;0m'))

    elif Jogador == 'PEDRA' and BotPart == 'TESOURA':
        print(emojize('\033[1;36mVocê Ganhou! (Eu escolhi Tesoura :scissors:))\033[0;0m'))

    elif Jogador == 'TESOURA' and BotPart == 'PAPEL':
        print(emojize('\033[1;36mVocê Ganhou! (Eu escolhi Papel :page_facing_up:))\033[0;0m'))

    # você perde
    else:
        print(emojize('\033[1;31mVocê perdeu! (Eu escolhi {} :rolling_on_the_floor_laughing:))\033[0;0m'.format(BotPart.title())))
    
    # perguntar se quer jogar novamente
    jogar_novamente = input('\nQuer jogar \033[1;32mnovamente\033[0;0m? (Y/n): ').lower()
    while jogar_novamente not in ['y', 'n']:
        jogar_novamente = input('\n\033[1;31mOpção inválida\033[0;0m. Quer jogar novamente? (Y/n): ').lower()
    if jogar_novamente == 'n':
        break
    print('\033[H\033[J')