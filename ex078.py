lista = []
MaiorValor = 0
MenorValor = 0
for Valores in range(5):
    lista.append(int(input(f'Digite um valor para a posição {Valores}: ')))
    if Valores == 0:
        MaiorValor = MenorValor = lista[Valores]
    else:
        if lista[Valores] > MaiorValor:
            MaiorValor = lista[Valores]
        if lista[Valores] < MenorValor:
            MenorValor = lista[Valores]
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {MaiorValor} na(s) posição(ões) ', end='')
for Posicao, Valores2 in enumerate(lista):
    if Valores2 == MaiorValor:
        print(f'{Posicao}... ', end='')
print()
print(f'O menor valor digitado foi {MenorValor} na(s) posição(ões) ', end='')
for Posicao, Valores2 in enumerate(lista):
    if Valores2 == MenorValor:
        print(f'{Posicao}... ', end='')
print()
