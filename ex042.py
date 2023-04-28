# Exercicio 042
print('=-'*25 + '=')
print('\n\n'+ ' '* 10, 'Analisador de Triângulos\n\n')
print('=-'*25 + '=\n')

LadoUm = float(input('\033[1;36mPrimeiro segmento\033[0m: '))
LadoDois = float(input('\033[1;36mSegundo segmento\033[0m: '))
LadoTres = float(input('\033[1;36mTerceiro segmento\033[0m: '))

if (LadoTres + LadoDois) > LadoUm and (LadoTres + LadoUm) > LadoDois and (LadoDois + LadoUm) > LadoTres:
		print('\nOs seguimentos acima \033[1;32mPODEM FORMAR\033[1;0m um triângulo!\n')
		if LadoUm == LadoDois == LadoTres:
			print('CLASSIFICAÇÃO: \033[1;44mEQUILÁTERO\033[0m')
		elif LadoUm != LadoDois != LadoTres != LadoUm:
			print('CLASSIFICAÇÃO: \033[1;44mESCALENO\033[0m')
		elif LadoUm == LadoDois != LadoTres or LadoDois == LadoTres != LadoUm or LadoTres == LadoUm != LadoDois:
			print('CLASSIFICAÇÃO: \033[1;44mISÓSCELES\033[0m')

else:
	print('\nOs seguimentos acima \033[1;41mNÃO PODEM FORMAR\033[0m um triângulo.')
