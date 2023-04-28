print('~'*40)
print('\n', ' '*10,'\033[1;36mLOJA\033[0;0m \033[1;33mROUBALHIAS\033[0;0m\n')
print('~'*40)

# Definindo as variáveis para: contagem de produtos acima de mil reais, Contador de loop, Preço do produto mais barato, nome do produto mais barato e valor total da compra.
Count_PriceOver1k = Total_Purchase_Price_Account = Counter_Loop = Cheaper_Product_Price = Cheaper_Product_Name = 0

while True:
    #Mini gambiarra para definirmos depois uma pergunta de continuação a cada vez que registrarmos um produto
    Continuation_Ask = ''
    
    #Perguntas sobre nome do produto e preço.
    Product_Name = str(input('Produto: '))
    Product_Price = float(input('Preço: R$'))
    
    #Nas linhas 17 e 18, faremos a contagem do loop e calcularemos o preço total da compra
    Counter_Loop += 1
    Total_Purchase_Price_Account += Product_Price
    
    #Descobrindo em qual loop será o produto mais barato e o preço dele, se for no primeiro loop, 'Cheaper_Product_Price' vai receber o valor do produto e 'Cheaper_Product_Name' vai receber o nome dele, caso não seja o primeiro faremos o mesmo até o usuário desejar sair.
    if Counter_Loop == 1:
        Cheaper_Product_Price = Product_Price
        Cheaper_Product_Name = Product_Name
    else:
        if Product_Price < Cheaper_Product_Price:
            Cheaper_Product_Price = Product_Price
            Cheaper_Product_Name = Product_Name
    
    #Se o valor do produto ultrapassar mill reais, o programa irá adicionar +1 a variável de contagem.
    if Product_Price >= 1000.00:
        Count_PriceOver1k += 1
     
    #Validação da resposta de continuação   
    while Continuation_Ask not in ['S', 'N']:
        Continuation_Ask = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()[0]
        print()
        
    #Parada do código.
    if Continuation_Ask == 'N':
        break

#Resultados finais.
print('~'*40)
print(f'\nO total gasto com estas compras foram R${Total_Purchase_Price_Account:.2f}')
print(f'Ao todo temos {Count_PriceOver1k} produtos acima dos mil reais.')
print(f'O produto mais barato foi {Cheaper_Product_Name} e custou R${Cheaper_Product_Price:.2f}')