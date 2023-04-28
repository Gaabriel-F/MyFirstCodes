#Exercicio 066

#Aqui teremos a definição das variáveis para Contagem de entradas e Soma das entradas.
Counter = Counter_For_Sum = 0

# Aqui se inicia o loop com while True, já que não sabemos o limite de quantos números o usuário deseja colocar e colocamos o número 999 como flag, para que pare o loop.
while True:
    User_input = int(input('Digite um número [999 para parar]: '))
    
    # Verificará se a entrada do usuário é 999, caso não for, fará os comandos que estão abaixo do if para Soma e Contagem.
    if User_input == 999:
        break
    Counter_For_Sum += User_input
    Counter += 1
    
# Aqui obteremos o resultado final.
print(f'\n\033[1;33mVocê digitou \033[1;31m{Counter}\033[1;33m números e a soma entre eles é \033[1;32m{Counter_For_Sum}\033[0;0m')