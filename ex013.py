#ex013 - salario
print()
tb = input('insira seu nome: ')
print()
slr = float(input('insira o seu salário para verificar o seu aumento: '))

amt = 1+15/100
ptds = slr*amt

print('Olá {} o seu salário de R${:.2f} recebeu um aumento de 15% e aumentou para R${:.2f} por mês.'.format(tb, slr, ptds))