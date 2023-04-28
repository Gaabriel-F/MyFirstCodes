# Exercicio 040 

NotaAluno1 = float(input('Digite a sua nota do primeiro semestre: '))
NotaAluno2 = float(input('Digite a sua nota do último semestre: '))

Media = (NotaAluno1 + NotaAluno2) / 2

if Media <= 5.0:
	print(f'\nSuas notas em ambos os semestres foram \033[1;34m{NotaAluno1}\033[0;0m e \033[1;34m{NotaAluno2}\033[0;0m e você acaba sendo \033[1;31mREPROVADO\033[0;0m\nMédia total de \033[1;44m{Media}\033[0;0m')
	
elif 5.0 <= Media <= 6.9:
	print(f'\nSuas notas em ambos os semestres foram \033[1;34m{NotaAluno1}\033[0;0m e \033[1;34m{NotaAluno2}\033[0;0m e você acaba entrando em \033[1;33mRECUPERAÇÃO\033[0;0m\nMédia total de \033[1;44m{Media}\033[0;0m')
	
else:
	print(f'\nSuas notas em ambos os semestres foram \033[1;34m{NotaAluno1}\033[0;0m e \033[1;34m{NotaAluno2}\033[0;0m e você foi \033[1;32mAPROVADO\033[0;0m!!\nMédia total de \033[1;44m{Media}\033[0;0m')