# Ex015 - coloquei sty pra ficar mais bonitim

from sty import fg, rs

PrimeiroAlerta = print(fg.red + 'Alerta!' + fg.rs + fg.yellow + ' Use somente números' + fg.rs)

print()

print()

DiasRodados = int(input('Por ' + fg.red + 'quantos dias' + fg.rs + ' o carro foi usado?: '))

print()

KilometrosRodados = float(input('Por ' + fg.red + 'quantos KM' + fg.rs + ' o carro rodou?: '))

vtl = (DiasRodados * 60) + (KilometrosRodados * 0.15)

print('O valor total a pagar é ' + fg.green + '{:.2f}'.format(vtl) + fg.rs)