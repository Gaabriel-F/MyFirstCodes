# Produção do jogo do Exercicio 028! - Parte 1 planejamento.

import random, time

MaquinaParte = random.randrange(0, 6)

print('\n\033[1;33mBem-vindo! \033[0;0meste arquivo python é um joguinho de adivinhação feito por \033[1;36mG.Felix!\033[0;0m\n')

PessoaParte = input('~-' * 20 + '\n\n\033[1;31mVamos dar inicio ao jogo!\033[0;0m\n\nEscolha \033[1;31muma\033[0;0m das opções abaixo para o seu palpite:\n\n\033[1;36m[0]\033[0;0m \033[1;35m[1]\033[0;0m \033[1;34m[2]\033[0;0m \033[1;33m[3]\033[0;0m \033[1;32m[4]\033[0;0m \033[1;30m[5]\033[0;0m\n\n' + '~-' * 20 + '\n\n\033[1;32m---> \033[0;0m')

# Parte 2 Arrumes para caso o usuario escolher uma opção errada

print('\n\033[1;33mCarregando...\033[0;0m\n')

time.sleep(2)

if int(PessoaParte) == MaquinaParte:
	print('Ihuulll!!! Você \033[1;32macertou\033[0;0m!!')

else:
		print(f'O número que eu escolhi foi \033[1;41m {MaquinaParte} \033[0;0m, infelizmente, \033[1;31mvocê não acertou\033[1;0m...')