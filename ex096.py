# Create a function to calculate the area.
def CalcArea(width, length):
    
    # Calculating the area.
    area = width * length

    # Displaying the results.
    print(f'\nThe area of this plot of land is {area}')


print(f'{"CALCULATING THE AREA":^12}')

# Variables to store the value of width and length.
Width = float(input("Width (m): "))
Length = float(input("Length (m): "))

# Passing the values of width and length to the CalcArea Function.
CalcArea(Width, Length)
