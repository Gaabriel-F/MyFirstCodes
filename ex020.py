# Exercicio 020

from random import shuffle

from sty import fg, rs

alunos = [input(fg.red + 'Digite' + fg.rs + f' o nome do aluno {i + 1}: ') for i in range(4)]

print('\n\nA ordem de apresentação' + fg.green + ' será' + fg.rs + ':')

shuffle(alunos)

for i, aluno in enumerate(alunos):
    print(f"{i + 1}. {aluno}")
