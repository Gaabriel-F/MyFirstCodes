SomaIdade = 0
IdadeMaisVelho = 0
Pessoa_Mais_Velha = ''
Womans20y = 0
for Pessoas in range(1, 5):
	print('-'*5, f'{Pessoas}ª PESSOA', '-'*5)
	NomePessoa = str(input('Nome: ')).strip().title()
	IdadePessoa = int(input('Idade: '))
	SexoPessoa = str(input('Sexo [M/F]: ')).strip()
	print()
	SomaIdade += IdadePessoa
	
	if Pessoas == 1 and SexoPessoa in 'Mm':
		IdadeMaisVelho += IdadePessoa
		Pessoa_Mais_Velha = NomePessoa
	
	if SexoPessoa in 'Mm' and IdadePessoa > IdadeMaisVelho:
		IdadeMaisVelho = IdadePessoa
		Pessoa_Mais_Velha = NomePessoa
		
	if SexoPessoa in 'Ff' and IdadePessoa < 20:
		Womans20y += 1
		
Media_idade = SomaIdade / 4

print(f'A média de idade do grupo é de {Media_idade:.0f} anos.')

if all(c in 'Ff' for c in SexoPessoa):
    print('Neste grupo não há nenhuma pessoa do sexo masculino.')
else:
	print(f'O homem mais velho do grupo se chama {Pessoa_Mais_Velha} e tem {IdadeMaisVelho} anos.')

if Womans20y == 1:
	print(f'Neste grupo temos apenas {Womans20y} mulher com menos de 20 anos.')

elif Womans20y == 0:
	print('Neste grupo todas as mulheres estão acima dos 20 anos')
	
else:
	print(f'Neste grupo temos um total de {Womans20y} mulheres com menos de 20 anos.')