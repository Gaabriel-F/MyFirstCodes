def CalcArea(width, length):
    area = width * length
    print(f'\nThe area of this plot of land is {area}')


print(f'{"CALCULATING THE AREA":^12}')
Width = float(input("Width (m): "))
Length = float(input("Length (m): "))

CalcArea(Width, Length)