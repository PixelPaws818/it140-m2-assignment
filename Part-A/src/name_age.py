"""Gets the user's name and age, then calculates and prints their approximate birth year."""

Input:
    #User name: A string representing the user's name, obtained from keyboard input.
    #User age: An integer representing the user's age, obtained from keyboard input.
    

Process:
    #Subtracts the user's age from the current yeart to calculate their birth year.

Output:
    #A formatted string printed to the console displaying the user's name and birth year..

Typical usage example:
    #What is your name? Alex    
    #How old are yu? 25
    #Hello Alex! You were born in 2001
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
   user_name=input("What is your name?')
   user_age=int(input("How old are you?'))

    # Calculate user's approximate birth year.
    birth_year=CURRENT_YEAR-user_age

    # Output personalized message with user's name and birth year.
   print(f'Hello{user_name}!You were born in{birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# Southern New Hampshire University. IT 140 Course Materials

