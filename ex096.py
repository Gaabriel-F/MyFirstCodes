# Create a function to calculate the area.
def CalcArea(width, length):
    """
    -------------------------------------------------
        Perform the multiplicaton between 2 values.

        Args:
            - width (float): receive the width of the area.

            - length (float): receive the length of the area.
        
        Returns:
            None
    -------------------------------------------------
    """
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
