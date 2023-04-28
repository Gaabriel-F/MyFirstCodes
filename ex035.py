r1=float(input('Digite o primeiro SEGMENTO: '))
r2=float(input('Digite o segundo SEGMENTO: '))
r3=float(input('Digite o terceiro SEGMENTO: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos digitados PODEM formar um TRIANGULO!')
else:
    print('Os segmentos digitados NÃO PODEM formar um TRIANGULO!')
