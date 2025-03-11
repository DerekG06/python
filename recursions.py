"""
Assignment: Calculating Factorials
Objective: Write a Python program using a recursive function to calculate the factorial of a number.
A recursive function is a function that calls itself to solve a problem.

Assignment Instructions:
Start by defining a function named factorial that takes one parameter, n, representing the number you're calculating the factorial for.
In your factorial function, first define the base case: n == 1 or n == 0, where the factorial is 1.
For the recursive step, return n * factorial(n-1) if n > 1.
Prompt the user for a non-negative integer and call factorial, printing the result.
"""


def factorial(n):
    if n == 1 or n == 0:
        # this is the base case, and once n == 1 or n == 0 then it will stop itself.
        return 1
    # the recursive here multiplies the user_num by -1 less than its current value, making the factorial
    return n * factorial(n - 1)


def main():
    user_num = int(input("Enter a non-negative integer: "))
    if user_num < 0:
        # in case the user does enter a negative integer, it will stop the program.
        print("You cannot enter a negative integer.")
    else:
        result = factorial(user_num)  # assigns result the integer 120
        print(f"The factorial of {user_num} is {result}")


main()
