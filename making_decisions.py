"""_summary_
    Write a Python program that uses if-else statements and:

Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward and user-friendly.
Remember:

Comment your code to explain the functionality of each section.
Handle edge cases, such as ages, precisely at the thresholds.
"""

# Converts user's age into an integer to be used in the later if and else statements
user_age = int(input("What is your age?: "))

# If user_age is above or equal to 16, it says you can drive. Otherwise if it's below then you can't.
if user_age >= 16:
    print("\nYou are old enough to drive.")
else:
    print("\nYou are not old enough to drive.")

# If user_age above or equal to 18, then you can vote, otherwise you cannot.
if user_age >= 18:
    print("You are able to vote.")
else:
    print("You are unable to vote.")

# If the user_age is above or equal to 21, then you can buy alcohol. Otherwise it prints that you cannot.
if user_age >= 21:
    print("You are able to purchase alcohol legally.")
else:
    print("You are not able to purchase alcohol legally.")

# If user_age is above or equal to 65 then they can get the discount, otherwise if they are below then they can't.
if user_age >= 65:
    print("You are eligible for the senior discount.")
else:
    print("You are not eligible for the senior discount.")
