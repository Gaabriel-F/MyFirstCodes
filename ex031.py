#Exercicio 031

distancia = float(input("Digite a distância de uma viagem (Km): "))
if distancia <= 200:
    valor = distancia * 0.50
    print(f'O valor da passagem será de R${valor:.2f}')
else:
    valor = distancia * 0.45
    print('O valor da passagem será de R${valor:.2f}')