#Exercicio 065, comecei definindo as variáveis que eu precisaria e os valores, defini também uma variável para que ela sirva como uma estrutura de funcionamento para o loop while
biggest_number = smallest_number = counter_for_sum = average_numeric = counter = 0

while True:# Aqui acabei usando um loop while True para uma condição interna pois acho mais simples assim, eu poderia usar o for também e iria obter o mesmo resultado, mas como estou apenas estudando while neste momento optei por fazer desta forma.
    # No loop while teremos a entrada do usuário que nós dará um número para que possamos trabalhar com ele logo abaixo.
    user_input = int(input('Digite um número: '))
    counter_for_sum = counter_for_sum + user_input # Aqui será feita a soma de todos os números que o usuário digitar para que possamos fazer a média no final
    counter += 1
    if counter == 1:# no primeiro loop o maior e menor número receberá o valor digitado pelo usuário.
        biggest_number = user_input
        smallest_number = user_input
        
    else: # Aqui faremos o aninhamento no else para verificar se os valores digitados pelo usuário são maiores ou menores.
        if user_input > biggest_number:# Aqui verifica se o valor digitado pelo usuário é maior que o número que já temos, se sim, a variável biggest_number passará a receber este valor, o mesmo ocorre abaixo porém, para números menores.
            biggest_number = user_input
			
        if user_input < smallest_number:
            smallest_number = user_input
            
    Continuation = input('\nDeseja continuar? [S/N]: ').lower().strip()[0]#input para terminar ou continuar o código.
    
    if Continuation == 's':
        print()
        continue
    if Continuation == 'n':
        break
    else:
        print('\n\033[1;31mErro\033[0;0m... Tente novamente!')
        break

if Continuation in ['s', 'n']:# condição produzida para caso a pessoa digite algo errado em "Continuation" e não aparecer nada, caso contrário aparecerá os dados normalmente.
    average_numeric = counter_for_sum / counter
    print(f'''\n\033[1;35mVocê digitou {counter} números e calculando a média deles teremos {average_numeric:.2f}\033[0;0m
\033[1;32mO maior valor digitado foi {biggest_number} e o menor foi {smallest_number}\033[0;0m''')