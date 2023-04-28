#Exercicio 075

NumFromUser1 = int(input('Digite um número: '))
NumFromUser2 = int(input('Digite um outro número: '))
NumFromUser3 = int(input('Digite mais um número: '))
NumFromUser4 = int(input('Digite mais um último número: '))

#Criando a tupla e variável para exibição de resultados finais
NumbersTuple = (NumFromUser1, NumFromUser2, NumFromUser3, NumFromUser4)
Count_Nines = NumbersTuple.count(9)

#Resultados finais.
print(f'\nOs valores digitados foram {NumbersTuple}')

#Fiz uso do operador ternário nesta parte do código pois achei que ficaria melhor desta forma.
print(f'O número 9 foi digitado {Count_Nines} vez(es).') if Count_Nines != 0 else print('O número 9 não foi digitado.')

#Na linha 19 como eu tinha a necessidade de criar essa variável para verificar a posição do número 3 eu precisaria usar a condição if desta forma já que se fosse através de um operador ternário caso não seja digitado 3 ocorreria um erro.
if 3 in NumbersTuple:
    PosOf3 = NumbersTuple.index(3)
    print(f'O primeiro número 3 foi digitado na {PosOf3+1}ª posição')
else:
    print('\nO número 3 não foi digitado.')
print('Os valores digitados que são pares são eles ', end='')
for i in NumbersTuple:
    if i % 2 == 0:
        print(i, end=' ')
print('')