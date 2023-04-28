# Tabuada V3

from time import sleep

#Iniciamos o loop pedindo a entrada do usuário e verificando se o número é igual ou menor que zero, caso não for, o código irá ocorrer perfeitamente.
while True:
    nm = int(input('\nDigite um número pra ver a sua tabuada\n(0 ou números negativos para parada): '))
    
    #flag para parada
    if nm <= 0:
        break
        
    print()
    print('-'*20)
    print()
    
    #Nessa parte, como sabemos o limite de quanto é uma tabuada comum, podemos assim, usar um loop for para a exibição de resultados.
    for c in range(1, 11):
        print(f'{nm}  X {c:2}  = {nm * c:1}')
        sleep(0.7)
    print()
    print('-'*20)