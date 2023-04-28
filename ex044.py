# Exercicio 044

print('='*9 + ' LOJAS ROUBALHIAS ' + '='*9)

ValorCompras = float(input('\nDigite o valor total das suas compras: R$'))
OpcaoCliente = int(input('''
\033[1;36m[1] À VISTA DINHEIRO/CHEQUE.\033[0;0m
\033[1;35m[2] À VISTA CARTÃO.\033[0;0m
\033[1;34m[3] 2x NO CARTÃO.\033[0;0m
\033[1;33m[4] 3x OU MAIS NO CARTÃO.\033[0;0m

\033[1;32mQual é a opção desejada\033[0m? '''))

if OpcaoCliente == 1:
	Desconto10 = ValorCompras - (ValorCompras * 0.1)
	print(f'\n\033[1;37mO valor total das compras é de \033[1;32mR${ValorCompras:.2f}\033[0;0m\033[1;37mPagando a vista em \033[1;42mdinheiro/cheque\033[0;0m, \033[1;37mvocê paga somente \033[1;32mR${Desconto10:.2f}\033[0m \033[1;37m(10% de desconto)\033[0;0m')

elif OpcaoCliente == 2:
	Desconto5 = ValorCompras - (ValorCompras * 0.05)
	print(f'\n\033[1;37mO valor total das compras é de \033[1;32mR${ValorCompras:.2f}\033[0;0m\n\033[1;37mPagando a vista em \033[1;42mdinheiro/cheque\033[0;0m, \033[1;37mvocê paga somente \033[1;32mR${Desconto5:.2f}\033[0;0m \033[1;37m(5% de desconto)\033[0;0m')
	
elif OpcaoCliente == 3:
	Desconto0 = ValorCompras / 2
	print(f'\n\033[1;37mO valor total das compras é de \033[1;32mR${ValorCompras:.2f}\n\033[1;37m\nPagando em \033[1;42m2x\033[0m \033[1;37mno cartão cada parcela fica \033[1;32mR${Desconto0:.2f}\033[0m')
	
elif OpcaoCliente == 4:
	Parcelas = int(input('\n\033[1;32mQuantas parcelas\033[0m? '))
	Juros = ValorCompras + (ValorCompras * 0.2)
	Parcelas_Cal = Juros / Parcelas
	print(f'\n\033[1;37mO valor total das compras é de \033[1;32mR${ValorCompras:.2f}\033[1;37m\nA compra será parcelada em \033[1;42m{Parcelas}x\033[1;0m \033[1;37mde \033[1;32mR${Parcelas_Cal:.2f}\033[1;0m')
	
else:
	print('\nOpcão invalida...')