# Exercicio 055

# Variáveis criadas para armazenar os valores maiores e menores digitados pelo usuário.
PesoMaior = 0
PesoMenor = 0

for Pesos in range(1, 6):
	Pesagem = float(input(f'Digite o peso da {Pesos}ª pessoa (Kg): '))
	if Pesos == 1: # O primeiro peso será o maior e menor no primeiro laço, nas próximas execuções do loop, o código verificara se o peso digitado é maior ou menor que o armazenado nas variáveis.
		PesoMaior = Pesagem
		PesoMenor = Pesagem
		
	else: # Para cada uma das próximas execuções do loop, o código verifica se o peso digitado é maior que o armazenado na variável PesoMaior. Se for, o novo peso é definido como o maior peso. O código também verifica se o peso digitado é menor que o armazenado na variável PesoMenor. Se for, o novo peso é definido como o menor peso.
		if Pesagem > PesoMaior:
			PesoMaior = Pesagem
			
		if Pesagem < PesoMenor:
			PesoMenor = Pesagem
			
print(f'\nO peso maior é de \033[1;32m{PesoMaior:.2f}Kg\033[0m\nE o peso menor é 0\033[1;32m{PesoMenor:.2f}Kg\033[0m')