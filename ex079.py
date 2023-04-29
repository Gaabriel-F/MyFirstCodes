Lista = []
while True:
    EntradaUsuario = int(input('Digite um valor: '))
    if EntradaUsuario not in Lista:
        Lista.append(EntradaUsuario)
        print('Valor adicionado com sucesso!!')
    else:
        print('Valores duplicados não serão adicionados!!')
    Continuar = input('Deseja continuar S/N: ').strip().lower()[0]
    while Continuar not in ['s', 'n']:
        Continuar = input('Deseja continuar S/N: ').strip().lower()[0]
        continue
    if Continuar == 's':
        continue
    if Continuar == 'n':
        break
print('-='*40)
print(f'\nOs valores digitados foram eles {sorted(Lista)}')