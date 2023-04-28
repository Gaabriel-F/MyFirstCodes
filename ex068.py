# Exercicio 068

import random, time

Winning_Streak = 0 #Variável para a contagen de vitórias.
print('~'*40)
print('\n', ' '*5,'VAMOS JOGAR \033[1;36mPAR\033[0;0m OU \033[1;33mÍMPAR\033[0;0m\n')
print('~'*40)
time.sleep(4)

#Aqui daremos início ao jogo através do loop while True.
while True:
  Bot_Part = random.randrange(0,11) # Variável para definir o valor que a maquina irá escolher.
  Win_or_Loose = 0 # Pequena gambiarra caso o usuario digite algo errado em um dos inputs para que o código leia esta variável
  User_input = input('\nDigite um número entre \033[1;35m[0 - 10]\033[0;0m: ')
  Pick_Even_Or_Odd = input('Par ou Ímpar? [P/Í]: ').upper().strip()[0]
  
  #Nesse 'if' iremos obter a soma entre a entrada do usuário e a parte da máquina + a validação do que foi digitado em 'User_input'
  if User_input.isnumeric() and int(User_input) in range(10):
     Win_or_Loose = int(User_input) + Bot_Part
   
  #Caso o usuário digite algo errado, ocorrerá os seguintes comandos.  
  else:
    time.sleep(2)
    print('\n\033[1;33mAlgo deu errado. Analisando...\033[0;0m')
    time.sleep(1.6)
    print('\n\033[1;31mEntrada inválida\033[0;0m! Digite apenas os números entre \033[1;31m0\033[0;0m e \033[1;31m10.\033[0;0m')
    time.sleep(3.5)
            
    #Limpa o console e interrompe o código.
    print('\033[H\033[J')
    continue
            
   #Nesse 'if' iremos obter a Escolha do usuário sobre Par ou Ímpar + a validação do que foi digitado em 'Pick_Even_Or_Odd', caso oque o usuário digite se enquadre neste if, ele simplesmente pulará para os próximos comandos no bloco do while True.
  if Pick_Even_Or_Odd.isalpha() and str(Pick_Even_Or_Odd) in ['P', 'I']:
    time.sleep(1.2)
    pass
    
  #Aqui no else irá ocorrer tbm uma mensagem de erro caso a validação do if acima não resulte em P ou I.
  else:
    time.sleep(2)
    print('\n\033[1;31mAlgo deu errado. Analisando...\033[0;0m')
    time.sleep(1.6)
    print('\n\033[1;31mEntrada inválida\033[0;0m! Para escolher Ímpar ou Par digite apenas: [\033[1;31mI\033[0;0m ou \033[1;31mP\033[0;0m]')
    time.sleep(3.5)
            
    #Limpa o console e interrompe o código.
    print('\033[H\033[J')
    continue
    
  #Nesta parte final será onde aplicaremos os resultados.
  
  #Nesse if iremos verificar se a váriável 'Pick_Even_Or_Odd' recebe 'P' pelo usuário, se sim, faremos o cálculo para saber se o número obtido é ou não Par, além também de adicionar +1 para a variável nomeada que criamos para sequência de vitórias.
  if Pick_Even_Or_Odd in ['P'] and Win_or_Loose % 2 == 0:
    print()
    print('='*60, f'\nVOCÊ escolheu {User_input} e o COMPUTADOR escolheu {Bot_Part}\n\033[1;31m[Total de {Win_or_Loose}]\033[0;0m\n\033[1;42mDEU PAR!\033[0;0m\n\033[1;32mVOCÊ VENCEU\033[0;0m!!!\nVamos jogar novamente...\n')
    print('='*60)
    print()
    Winning_Streak += 1 # Variável nomeada para nossa sequência de vitórias.
    time.sleep(1.7)
            
   #Já nesse elif iremos verificar se a soma armazenada na váriavel 'Win_or_Loose' divida por 2 nos resultará em uma divisão com resto acima de 0, se sim, o seguinte bloco de códigos acontecerá e haverá a interrupção do loop.
  elif Pick_Even_Or_Odd in ['P'] and Win_or_Loose % 2 > 0:
    print()
    print('='*60, f'\n\nVOCÊ escolheu {User_input} e o COMPUTADOR escolheu {Bot_Part}\n\033[1;31m[Total de {Win_or_Loose}]\033[0;0m\n\033[1;42mDEU ÍMPAR!\033[0;0m\n\033[1;31mVOCÊ PERDEU\033[0;0m!\n')
    print('='*60)
    print()
    break

# Nesse 'else:', vai ocorrer exatamente da mesma forma como os if's acima, apenas oque mudará é que isso só vai acontecer caso o usuário escolha 'I' como opção.
  else:
    if Pick_Even_Or_Odd in ['I'] and Win_or_Loose % 2 > 0:
      print()
      print('='*60, f'\n\nVOCÊ escolheu {User_input} e o COMPUTADOR escolheu {Bot_Part}\n\033[1;31m[Total de {Win_or_Loose}]\033[0;0m\n\033[1;42mDEU ÍMPAR!\033[0;0m\n\033[1;32mVOCÊ VENCEU\033[0;0m!!!\nVamos jogar novamente...\n')
      print('='*60)
      print()
      Winning_Streak += 1
      time.sleep(1.7)
                    
    else:
      print()
      print('='*60, f'\n\nVOCÊ escolheu {User_input} e o COMPUTADOR escolheu {Bot_Part}\n\033[1;31m[Total de {Win_or_Loose}]\033[0;0m\n\033[1;42mDEU PAR!\033[0;0m\n\033[1;31mVOCÊ PERDEU\033[0;0m!\n')
      print('='*60)
      print()
      break
      
# Final do código.
print('\033[1;31mGAME OVER...\033[0;0m', end='')
print(f' Você venceu \033[1;44m{Winning_Streak}\033[0;0m vezes.')
