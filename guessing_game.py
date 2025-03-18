"""
In this assignment, you will create a Python program that generates a random number between 1 and 100. 
Your program should allow the user to guess the number, and provide feedback on how close their guess is to the actual number.

Assignment Objectives:
    Use the random module to generate a random number.
    Implement a while loop to allow continuous guessing until the correct number is guessed.
    Use the abs() function to determine the difference between the guess and the actual number.
    Provide feedback based on the proximity of the guess to the actual number:
    If the difference is within 5, print "Very Hot".
    If the difference is within 15, print "Hot".
    If the difference is within 25, print "Cool".
    If the difference is more than 25, print "Cold".
    Make sure to call the main function!
    After completing the program, upload it to your GitHub repository.
    Submit the link to your GitHub repository in Canvas.

Task Details:
    Import the random module and use it to generate a random number between 1 and 100.
    Write a while loop that allows the user to enter a guess for the number.
    Inside the loop, use the abs() function to calculate the absolute difference between the guess and the actual number.
    Provide feedback based on the computed difference (e.g., "Very Hot" for close guesses).
    The loop should continue until the user guesses the correct number.

Additional Notes:
    The abs() function is a built-in Python function used to calculate the absolute value of a number. 
    The absolute value of a number is its distance from zero on the number line, regardless of direction. 
    For example, abs(-5) and abs(5) both return 5.
"""

import random


def main():
    # A number between 1 and 100 is created and stored in "secret_number"
    secret_number = random.randint(1, 100)
    print("Guess the number between 1 and 100!")

    while True:
        # The user's guesses are entered here each time they attempt a new number.
        guess = int(input("Enter your guess: "))

        # Always gives a positive number to make sure nothing in the program gets broken.
        difference = abs(secret_number - guess)

        # All the logic to decide which response is used based on the number from above.
        if difference == 0:
            print("Congratulations! You guessed the correct number.")
            break  # Finally ends the program
        elif difference <= 5:
            print("Very Hot")
        elif difference <= 15:
            print("Hot")
        elif difference <= 25:
            print("Cool")
        else:
            print("Cold")


main()
