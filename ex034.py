#Ex 034

Salario = float(input('Digite o seu salário: '))
if Salario > 1250.00:
    Aumento = Salario * 0.1
    Salario += Aumento
    print(f'Seu salario passará a ser {Salario:.2f} após o aumento de 10%.')
elif Salario <= 1250.00:
    Aumento = Salario * 0.15
    Salario += Aumento
    print(f'Seu salario passará a ser {Salario:.2f} após o aumento de 15%.')