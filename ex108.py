from utils import functions

numByUser = int(input("Enter a monetary value: R$"))
print(f'The double of R${numByUser:.2f} is R${functions.Double(numByUser):.2f}')
print(f'The half of R${numByUser:.2f} is R${functions.Half(numByUser):.2f}')
print(f'Reducing the value by 10% will be R${functions.ReduceByPercent(numByUser, 10):.2f}')
print(f'Adding 10% to the value will be R${functions.AddByPercent(numByUser, 10):.2f}')
