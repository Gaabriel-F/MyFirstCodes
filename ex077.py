TUPLA = ('APRENDER', 'ESTUDAR', 'TRABALHAR', 'MELHORAR', 'VIVER', 'CRESCER', '\033[1;31mPROGRAMAR\033[0;0m')

for PosiçãoDaPalavra in TUPLA:
    print(f'\nNa palavra {PosiçãoDaPalavra} as vogais são: ', end='')
    for Vogais in PosiçãoDaPalavra:
        if Vogais.upper() in 'AEIOU':
            print(Vogais, end=' ')