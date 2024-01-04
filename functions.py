def Summary(price = 0, adding = 0, reducing = 0):
    print('-'*30)
    print(f'{"ANALIZING THE VALUE":^30}')
    print('-'*30)

    Double = price * 2
    Half = price / 2
    
    percent1 = (price * adding) / 100
    resultAdding = price + percent1

    percent2 = (price * adding) / 100
    resultReducing = price - percent2

    print(f'Analized price: \t{price:.2f}')
    print(f'Twice the price: \t{Double:.2f}')
    print(f'Half the price: \t{Half:.2f}')
    print(f'adding {adding}%: \t\t{resultAdding:.2f}\t')
    print(f'reducing {reducing}%: \t\t{resultReducing:.2f}')