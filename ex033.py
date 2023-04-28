#Exercicio 033

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o ultimo valor: '))
lista = [n1, n2, n3]
lista = sorted(lista)
print(f'\nDos valores digitados, o maior é {lista[2]} e o menor é {lista[0]}')