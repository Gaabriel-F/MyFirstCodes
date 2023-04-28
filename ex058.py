# Parte de importações, definições de valores e variaveis

import random, time, emoji

while True:
	MaquinaParte = random.randrange(0, 6)
	print('\n\033[1;33mBem-vindo! \033[0;0meste arquivo python é um joguinho de adivinhação feito por \033[1;36mG.Felix!\033[0;0m\n')
	time.sleep(2.2)
	
	# Parte 2: Definição do input e ajustes para possiveis erros
	
	while True:
	    Num_Tentativas = 0
	    print('\033[H\033[J')
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
	
	if int(PessoaParte) != MaquinaParte:
		Num_Tentativas += 1
	
	if int(PessoaParte) == MaquinaParte:
	    print(emoji.emojize('Você \033[1;32macertou\033[0;0m!! Dessa vez você me pegou... :cowboy_hat_face: '))
	    time.sleep(1.2)
	    print('\n\033[1;32mDe primeira\033[0m!!!')
	    
	    print('\033[H\033[J')
	    
	# Aqui abaixo mostrará que o usuário errou e pedirá novamente o input do mssmo, assim fazendo a contagem pela variável 'cont', enquanto o usuario não atender o requisito do while o programa continuará pedindo um novo palpite e contando quantas vezes ele erra
	
	else:
		time.sleep(0.9)
		print('\033[1;31mParece que você errou, tente novamente')
		while int(PessoaParte) != MaquinaParte:
			try:
				PessoaParte = int(input('\n\033[1;35mQual é o seu novo palpite?\033[0m: '))
			except ValueError:
				time.sleep(1.2)
				print('\n\033[1;31mEntrada inválida\033[0;0m! Digite apenas os números entre \033[1;31m0\033[0;0m e \033[1;31m5.\033[0;0m')
				time.sleep(1.1)

			if MaquinaParte > int(PessoaParte):
				time.sleep(0.7)
				print('\n\033[1;33mMais... Tente o seu palpite novamente\033[0m')
				Num_Tentativas +=1
				
			if MaquinaParte < int(PessoaParte):
				time.sleep(0.7)
				print('\n\033[1;34mMenos... Tente o seu palpite novamente\033[0m')
				Num_Tentativas +=1	
				
			if int(PessoaParte) == MaquinaParte:
				print(emoji.emojize('\nVocê \033[1;32macertou\033[0;0m!! Dessa vez você me pegou... :cowboy_hat_face: '))
				Num_Tentativas += 1
				break
		time.sleep(1.8)								
		print(f'\n\033[1;34mVocê levou \033[43;1;30m{Num_Tentativas}\033[0;0m \033[1;34mtentativas para acertar o número escolhido.\033[0m')
		time.sleep(2.0)
	print('\033[H\033[J')	
	jogar_novamente = input('\nJogar \033[1;32mnovamente\033[0;0m? (S/N): ').lower().strip()[0]
	while jogar_novamente not in ['s', 'n']:
		jogar_novamente = input('\n\033[1;31mOpção inválida\033[0;0m. Quer jogar novamente? (S/N): ').lower().strip()[0]
		continue
	if jogar_novamente == 's':
		print('\033[H\033[J')
		continue
	if jogar_novamente == 'n':
		break
