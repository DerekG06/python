"""
Instructions
Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
Identify Potential Errors: Consider errors that might occur with non-numeric input.
Add Exception Handling: Implement try and except blocks to catch a ValueError. Handle incorrect data types with an error message.
Test Your Code: Ensure the exception handling works correctly with various inputs.
GitHub Upload: Upload your py file to GitHub and hand in the link
"""


# Simple Python program to calculate the square of a number


def square_number():
    try:  # Main code that requests user inputs
        number = input("Enter an integer to square: ")
        squared_number = int(number) ** 2
    except ValueError:  # Tries to catch ValueErrors and outputs this message
        print("Please enter an integer, the program only uses an integer!")
    else:  # If there are no ValueErrors, the program will show the correct squaring of a number.
        print(f"The square of {number} is {squared_number}.")


square_number()
