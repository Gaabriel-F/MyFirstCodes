# Exercicio 027

NomeUsuario = str(input('Digite seu nome completo: ')).strip()

Nsplit = NomeUsuario.split()

print(f'\nOii, muito prazer em te conhecer {Nsplit[0]}!\n\nPelo oque estou vendo aqui seu primeiro nome é {Nsplit[0]} e seu último nome é {Nsplit[-1]}.')
