#Exercicio 071

print('×-~'*15 + '×')
print()
print(' '*13, '\033[1;33mBANCO \033[1;36mRAFF \033[1;36mi\033[1;33m&\033[1;36mA\033[0;0m')
print()
print('×-~'*15 + '×\n')
Withdrawal_Amount_User = int(input('Quanto deseja sacar?: R$'))
Total_Amount = Withdrawal_Amount_User
Banknotes = 50
Counter_For_Banknotes = 0
print()
while True:
    if Total_Amount >= Banknotes:
        Total_Amount -= Banknotes
        Counter_For_Banknotes += 1
    else:
        if Counter_For_Banknotes > 0:
            print(f'Total de {Counter_For_Banknotes} cédulas de R${Banknotes:}')
        if Banknotes == 50:
            Banknotes = 20
        elif Banknotes == 20:
            Banknotes = 10
        elif Banknotes == 10:
            Banknotes = 1
        Counter_For_Banknotes = 0
        if Total_Amount == 0:
            break
            
print()
print('×-~'*17 + '×')
print('\nTenha um Bom Dia e volte sempre! - \033[1;33mBANCO \033[1;36mRAFF \033[1;36mi\033[1;33m&\033[1;36mA\033[0;0m')