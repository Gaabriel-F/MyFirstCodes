#Variaveis criadas para atuarem na contagem do exercicio.
Counter_Age_Over18 = Male_Count = Counter_Woman_Under20 = 0


while True:
    print('-'*40, '\n')
    print(' '*8 + 'CADASTRE UMA PESSOA')
    print('\n' + '-'*40)
    print()
    Get_Gender_User = ''
    #Aqui será onde eu irei pedir a entrada de idade que o usuário for cadastrar e logo abaixo através farei a seguinte verificação, escolhi usar um else aninhado de um if ao invés de colocar o 'Get_Age_User' antes de um loop while abaixo, pois foi a unica forma que pensei no momento de fazer isso.
    Get_Age_User = input('Idade: ').strip()
    if Get_Age_User.isnumeric(): #Aqui verificará se é True, se não for cairá no else e ele verificará também se é valido e fara a contagem de acima de 18 anos, através desta variavel Counter_Age_Over18
        if int(Get_Age_User) >= 18:
            Counter_Age_Over18 += 1
        pass
    else:
        while Get_Age_User.isalpha():
            Get_Age_User = input('Idade: ').strip()
            if Get_Age_User.isnumeric() and int(Get_Age_User) >= 18:
                Counter_Age_Over18 += 1
        if Get_Age_User is Get_Age_User.isnumeric():
            break
            
    #Inicio da verificação do gênero, juntamente com a contagem de homens cadastrados + contagem de mulheres abaixo dos 20 anos de idade.
    while Get_Gender_User not in ['M', 'F']:
        Get_Gender_User = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if Get_Gender_User == 'M':
            Male_Count += 1
            
        if Get_Gender_User == 'F':
            if Get_Gender_User == 'F' and int(Get_Age_User) < 20:
                Counter_Woman_Under20 += 1

    #print para separação do input abaixo.
    print('\n' + '-'*40)
    
    #Faremos o mesmo método também visto acima (das linhas 13 até 23) para a verificação de parada ou continuada e tratar possíveis erros de entrada do usuário.
    Continuation_Option = str(input('\nDeseja continuar? [S/N]: ')).upper().strip()[0]
    print()
    if Continuation_Option in 'SN':
        if Continuation_Option == 'S':
            continue
        if Continuation_Option == 'N':
            break
            
    else:
        while Continuation_Option not in 'SN':
            Continuation_Option = str(input('\nDeseja continuar? [S/N]: ')).upper().strip()[0]
            print()
        if Continuation_Option == 'N':
            break
            
#por fim, temos o cálculo final com amostragem dos dados.
print(f'\033[1;34mAo todo temos {Counter_Age_Over18} pessoas na maioridade\033[0;0m\n\033[1;32m{Male_Count} Homens cadastrados\033[0;0m\n\033[1;31mE por fim, {Counter_Woman_Under20} mulheres abaixo dos 20 anos\033[0;0m.')