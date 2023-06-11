def vote(birth):
    """
    -------------------------------------------------

        Checks the voting status based on the provided year of birth.

        Args:
            - birth (int): The year of birth as an integer value.
        
        Returns:
            str: A message indicating the voting situation based on age.
        
        Raises:
            None

        Examples:
            >>> vote(1990)
            'WITH 31 YEARS OLD SITUATION \033[1;32mMandatory Voting\033[0;0m'

            >>> vote(2007)
            'WITH 16 YEARS OLD SITUATION \033[1;33mOptional Voting\033[0;0m'

            >>> vote(2012)
            'WITH 11 YEARS OLD SITUATION \033[1;31mNot Eligible to Vote\033[0;0m'

    -------------------------------------------------
    """

    from datetime import datetime
    
    # Calculating the user's age
    current_year = datetime.now().year
    ageUser = current_year - birth
    
    # Checking if the vote is mandatory.
    if 18 <= ageUser <= 70:
        return f"\nWITH {ageUser} YEARS OLD\nSITUATION \033[1;32mMandatory Voting\033[0;0m"
    
    # Checking if the vote is optional.
    elif 16 <= ageUser < 18 or ageUser >= 71:
        return f"\nWITH {ageUser} YEARS OLD\nSITUATION \033[1;33mOptional Voting\033[0;0m"
        
    # Checking if the user is underage.
    elif 0 <= ageUser <= 15:
        return f"\nWITH {ageUser} YEARS OLD\nSITUATION \033[1;31mNot Eligible to Vote\033[0;0m"
        
        
# Main Program.
# Request the input of birth year to the user.
birthYear = int(input('Enter your birth year: '))

# Passing the parameter.
print(vote(birthYear))
