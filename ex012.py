#ex012 - roupa e afins

rp = str(input('Insira o nome do produto: '))
print()
v = float(input('Insira o valor do produto: '))
print()
sale = v*15/100
ptd = v-sale
sale0 = ptd-v

print('O valor liquido da {} é R${:.2f} sem impostos. O valor economizado através do desconto foi de R${:.2f}'.format(rp, ptd, sale0))