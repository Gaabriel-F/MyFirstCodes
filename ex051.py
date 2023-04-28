# Exercicio 51
print('='*30, '\n\n     10 TERMOS DE UMA PA\n\n' + '='*30)
Primeiro_Termo = int(input('Digite o primeiro termo da PA: '))
Razao_PA = int(input('Digite a razão da PA: '))
DécimoTermo = Primeiro_Termo + (10 - 1) * Razao_PA
print()
for C in range (Primeiro_Termo, DécimoTermo + Razao_PA, Razao_PA):
	print(C, end = ' ➞ ')
print('ACABOU')