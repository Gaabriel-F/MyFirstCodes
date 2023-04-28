#ex004
a = input('Digite algo: ')
print('Qual é o tipo da coisa digitada?', type(a))
print(f'''Só tem espaços? {a.isspace()}
É número? {a.isnumeric()}
É alfabético? {a.isalpha()}
É alfanúmerico? {a.isalnum()}
Está tudo maiúsculo? {a.isupper()}
Está tudo minúsculo? {a.islower()}
Está capitalizado? {a.istitle()}''')