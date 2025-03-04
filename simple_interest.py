"""
    Objective:
Write a Python function named calculate_interest that computes and returns simple interest based on given parameters.

Background
Simple interest is calculated using the formula:

Simple Interest = (Principal Amount x Rate of Interest x Time) / 100

Function Requirements
A main function should control the logic of the program
Create and call a function should be named calculate_interest.
It should take three parameters that you get from the user:
principal - The initial amount.
rate - The annual interest rate (percentage).
time - The investment duration in years.
Use the return keyword to send back the computed interest to a variable in the main function.
Print the result using formatted strings in the main function.
Example
If you call calculate_interest(1000, 5, 2), the function should return 100 as the simple interest.

Task Instructions
Define the function calculate_interest with appropriate parameters.
Apply the formula to calculate the simple interest.
Return the calculated interest.
Print the result using an f-string:
print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")
"""

# Here all the previous functions and variables are brought into main(), which is called at the end of the program


def main():
    principal, rate, time = get_values()
    simple_interest = calculate_interest(principal, rate, time)
    print(
        f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${simple_interest:,.2f}.")

# This function receives the user's inputs and uses them in main() and calculate_interest()


def get_values():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time in years: "))
    return principal, rate, time

# Uses the values the user entered in get_values() to calculate the simple interest


def calculate_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest


main()
