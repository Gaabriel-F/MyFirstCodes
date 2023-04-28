# Exercicio 025

Sme = str(input('Digite o seu nome completo: '))
print('\n\033[1;32;40mChecando\033[0;0m... Veremos se há "Silva" no seu nome.\n')

# Definição do ambiente para as instrucoes do programa

Sd = Sme.upper().split()

tf = 'SILVA' in Sd

# Instrucoes para o codigo

if tf == True:
	print(f'\nSeu nome é {Sme.strip().title()} e ele tem "Silva" !')

else:
		print(f'\nSeu nome é {Sme.strip().title()} e ele parece não ter "Silva".')