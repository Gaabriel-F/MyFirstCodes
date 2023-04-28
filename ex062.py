# Exercicio 62
print('='*30, '\n\n     10 TERMOS DE UMA PA\n\n' + '='*30)

Primeiro_Termo = int(input('Digite o primeiro termo da PA: '))
Razao_PA = int(input('Digite a razão da PA: '))

LimitePA = 0 #Variável para a contagem que irá até 10 e pausará o loop abaixo.
Contador1termo = Primeiro_Termo# Variável criada para que receba o primeiro termo da pa e no loop ela será somada a razão para nos mostrar a progressão da PA, pulando os números conforme a razão.
Contagem = 0
Limite2 = 1
print()
while not LimitePA == 10:# Enquanto LimitePA não for igual à 10 obteremos este resultado do print abaixo, além de ser adicionado "1" para o limite, assim chegando em 10 e parando o loop while.
	print(f'{Contador1termo}', end= ' ➞ ')
	Contador1termo += Razao_PA
	LimitePA += 1
	Contagem += 1
print('PAUSA')

#A Variavel Limite2 enquanto ela ser == 1 ou mais ela ativará o loop e nos pedira o input até que o usuario digite 0 para parar, para a contagem e exibição da razão temos o mesmo cálculo do loop acima.

while not Limite2 == 0:
	Limite2 = int(input('\n\n\033[1;32mDeseja ver mais alguns termos?\nDigite (0) caso deseje parar!\n\n\033[1;34m--->\033[0;0m '))
	print()
	for Teste in range(1, Limite2+1):
		Contagem += 1
		Contador1termo += Razao_PA
		print(f'\033[35m{Contador1termo} \033[0;0m', end= ' ➞  ')
		
		#Aqui é Se limite for maior que zero, printar isso, se não, não mostrará nada
		
	if Limite2 > 0:
		print('PAUSA')
print(f'\033[1;33mACABOU\033[0;0m... Foi lhe mostrado \033[1;32m{Contagem}\033[0;0m termos durante a execução do código.')