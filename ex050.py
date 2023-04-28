soma = 0
cont = 0
for c in range(1, 7):
	Num = int(input(f'Digite o {c}° número: '))
	if Num % 2 == 0:
		soma += Num
		cont += 1
print(f'\nVocê informou {cont} números PARES e a soma entre eles é equivalente a {soma}')
		