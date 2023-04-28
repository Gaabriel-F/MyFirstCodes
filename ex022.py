# Exercicio 022

NomePessoa = str(input('Digite seu nome completo: ')).strip()

NPsplit = NomePessoa.split()
print('Analisando nome...')
print('Seu nome em maiúsculo é', NomePessoa.upper())
print('Seu nome em minúsculo é', NomePessoa.lower())
print('Seu nome ao todo tem {} letras'.format(len(NomePessoa) - NomePessoa.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(NPsplit[0], len(NPsplit[0])))