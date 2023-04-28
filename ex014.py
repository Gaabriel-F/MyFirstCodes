from sty import fg, bg, ef, rs

# Primeira opção

cls = str(input('Digite a medida para a conversão, se atente a escrever exatamente como proposto abaixo:' + fg.yellow + ' \n \n Celsius - °C \n Fahrenheit - °F \n \n' + fg.rs + 'Digite a opção desejada:  '))

print() 
print()

# Instruções primeira opção

if cls == "°C":
	print(fg.yellow + 'a opção escolhida foi' + fg.green + ' {}'.format(cls) + fg.rs) 
	
elif cls == "°F":
		print(fg.yellow + 'a opção escolhida foi' + fg.green + ' {}'.format(cls) + fg.rs)  
		
else:
	print(fg.red + 'a opção escolida é invalida!' + fg.rs + ' Digite exatamente como é mostrado acima.')

# Atuando como 'parágrafos ou espaçamentos'


print()
print() 
print()


# Segunda opção

cld = str(input(f'Você quer transformar {cls} para qual medida dentre essas opções?' + fg.yellow + '\n \n Celsius - °C \n Fahrenheit - °F \n \n' + fg.rs + 'Digite a opção desejada: '))

print()

# Instruções segunda opção

if cld == "°C":
	print(fg.yellow + 'a opção escolhida foi' + fg.green + ' {}'.format(cld) + fg.rs) 
	
elif cld == "°F":
	print(fg.yellow + 'a opção escolhida foi' + fg.green + ' {}'.format(cld) + fg.rs)

else:
	print(fg.red + 'a opção escolida é invalida!'+ fg.rs + ' Digite exatamente como é mostrado acima.')

print()
print()
print()

cpd = float(input('Digite a quantidade a ser convertida: °'))
()
print()
print()

# Optei pela resolução desta forma mais simples

rstd1 = (cpd * 9/5) + 32
	
rstd2 = (cpd-32) * 5/9


# Ajustes e resultados

if cld == "°F" and cls == "°F":
  print(fg.blue + 'A temperatura é de  {} °F '.format(cpd) + fg.rs)

elif cls == "°F":
  print(fg.blue + 'Convertendo a temperatura de {:.2f}{} para °C a medida obtida é correspondente a: {:.2f} °C'.format(cpd, cls, rstd2) + fg.rs)

elif cls == "°C" and cld == "°F":
  print(fg.blue + 'Convertendo a temperatura de {:.2f}°C para °F a medida obtida é correspondente a: {:.2f} °F'.format(cpd, rstd1) + fg.rs)

elif cls == "°C" and cld == "°C":
  print(fg.blue + 'A temperatura é de  {} °C '.format(cpd) + fg.rs)

else:
  print(fg.red + 'Erro na conversão!' + fg.rs + ' Digite exatamente como esta escrito nas opções listadas!')
