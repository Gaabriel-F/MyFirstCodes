while True:
	print('='*36, '\n')
	print(' '*6, 'SEQUÊNCIA DE FIBONACCI\n')
	print('='*36, '\n')
	NumeroUsuario = int(input('Digite um número: '))
	PrimeiroTermo = 0
	SegundoTermo = 1
	print('')
	if NumeroUsuario == 0:
		break
	if NumeroUsuario == 1:
		print('0 - ', end='')
		break
	elif NumeroUsuario <= 2:
		print('0 - 1 -', '', end='')
		break
	if NumeroUsuario >= 3:
		print('0 - 1 -', '', end='')
		for ShowTermos in range(NumeroUsuario-2):
			TerceiroTermo = PrimeiroTermo + SegundoTermo
			PrimeiroTermo = SegundoTermo
			SegundoTermo = TerceiroTermo
			print(TerceiroTermo, end=' - ')
		break
print('FIM')
