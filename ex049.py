# Tabuada V2

from time import sleep
nm = int(input('Digite um número pra ver a sua tabuada: '))
print()
print('-'*20)
print()
for c in range(1, 11):
	print(f'{nm}  X {c:2}  = {nm * c}')
	sleep(0.7)
print()
print('-'*20)