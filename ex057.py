# Exercicio 057 - Estrutura While

SexoPessoa = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while SexoPessoa not in 'MmFf': # Aqui verificará se o input do usuário atende ao requerido que é M, m, F ou f, caso não atenda isto irá se repetir infinitamente
	print('\n\033[1;31mOpção inválida\033[0m... Tente novamente!!')
	SexoPessoa = str(input('\nDigite novamente o seu sexo: ')).strip().upper()[0]


print(f'\nSexo {SexoPessoa.upper()} registrado com sucesso!!')