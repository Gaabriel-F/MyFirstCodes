from utils import functions

numByUser = int(input("Enter a value: "))
print(f'The double is {functions.Double(numByUser)}')
print(f'The half is {functions.Half(numByUser)}')
print(f'Reducing the value by 10% will be {functions.ReduceByPercent(numByUser, 10)}')
print(f'Adding 10% to the value will be {functions.AddByPercent(numByUser, 10)}')
