# Exercicio 036
from time import sleep

print('Programa \033[1;32mEMPRÉSTIMOS\033[0m \033[1;33mBRASIL\033[0m')

ValorDaCasa = float(input('\nDigite o valor da casa\033[0m: R$'))
SalarioPedidor = float(input('\nQuanto você recebe?: R$'))
AnosForPay = int(input('\nDeseja pagar em quantos anos?: '))

Prestacao = ValorDaCasa / (AnosForPay * 12)

print(f'Para pagar uma casa de R${ValorDaCasa:.2f} em {AnosForPay} anos a prestação será de R${Prestacao:.2f} mensais.\n\nAguarde pelo status do seu pedido de empréstimo.\n')

sleep(2)

if Prestacao > SalarioPedidor * 0.3:
	print('STATUS: \033[1;31mNEGADO\033[0;0m')
else:
	print('STATUS: \033[1;32mCONCEDIDO\033[0;0m')