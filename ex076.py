#Exercicio 076

print('-'*50)
print(f'{"TABELA DE PREÇOS":^45}')
print('-'*50)
print("")
ProductsList = ('\033[1;34mLapis\033[0m', 1.70, '\033[1;34mBorracha\033[0m', 1, '\033[1;34mApontador\033[0m', 1.50, '\033[1;34mEstojo\033[0m', 10, '\033[1;34mSketchbook\033[0m', 50)
for ItemIndexes in range(0, len(ProductsList)):
    if ItemIndexes % 2 == 0:
        print(f'{ProductsList[ItemIndexes]:.<30}', end='')
    else:
        print(f'R$\033[1;32m{ProductsList[ItemIndexes]:>7.2f}\033[0;0m')
