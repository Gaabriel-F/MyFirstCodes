# Exercicio 054
from datetime import date

#Parte para calcular a seguir idade e contabilizar como maior ou de menor.
AnoAtual = date.today().year
Contador1 = 0 
Contador2 = 0

#Aqui se inicia a estrutura de repetição FOR para requerir o ano de nascimento e definir a condição para contagem de idade
for Pessoas in range(1, 8):
	
	NascPessoa = int(input(f'Em qual ano a {Pessoas}ª pessoa nasceu?: '))
	if AnoAtual - NascPessoa >= 18:
		Contador1 += 1
	else:
		Contador2 += 1
		
#Por fim obtemos os valores e assim mostramos quantos são maiores de idade e quantos são menores.		
print(f'Ao todo tivemos {Contador1} pessoas maiores de idade\nE também {Contador2} pessoas menores de idade')