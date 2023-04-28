# Exercicio 043

PesoKG = float(input('Digite o seu peso (Kg): '))
PessoaAltura = float(input('Digite a sua altura (m): '))

CalcIMC = PesoKG / (PessoaAltura ** 2)
print(f'\nO \033[1;44mIMC\033[0m desta pessoa é de \033[1;35m{CalcIMC:.1f}\033[0m')
if CalcIMC <= 18.4:
	print('CLASSE \033[1;31mABAIXO DO PESO\033[0m')
	
elif 18.5 <= CalcIMC < 25.0:
	print('CLASSE \033[1;32mPESO IDEAL\033[0m')
	
elif 25.1 <= CalcIMC < 30.0:
	print('CLASSE \033[1;33mSOBREPESO\033[0m')
	
elif 30.1 <= CalcIMC < 40:
	print('CLASSE \033[1;41mOBESIDADE\033[0m')
	
elif CalcIMC >= 40:
	print('CLASSE \033[1;41mOBESIDADE MORBIDA\033[0m, \033[1;33mCuidado\033[0m!')