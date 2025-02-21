'''
In this exercise, you will practice using logical operators (and, or, not) in Python. 
Your task is to create a program that prompts the user for two integer inputs and then demonstrate the use of these operators.

User Input: Start by asking the user to input two distinct integers. 
Logical Operators: Implement six different logical comparisons using the input integers.
Include two examples for each of the following operators:
    and
    or
    not
Display Results: Print the logical statement and its result for each comparison.
Guidelines for Logical Comparisons:
Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
Try to use comparisons that could yield different results based on user input.
'''

# The user is asked to input 2 integers so it can later be used in the logical operations.
user_num1 = int(input("Please enter your first number: "))
user_num2 = int(input("Please enter your second number: "))

# Using "and" logic operation to see if both numbers are bigger than 0 and smaller than 150.
if user_num1 > 0 and user_num1 > 0:
    print("Both of your numbers are greater than 0: True")
else:
    print("Both of your numbers are greater than 0: False")

if user_num1 < 150 and user_num2 < 150:
    print("Both of your numbers are less than 150: True")
else:
    print("Both of your numbers are less than 150: False")

# Using "or" to see if one number is negative and if its even.
if user_num1 < 0 or user_num1 < 0:
    print("One number is negative: True")
else:
    print("One number is negative: False")

if user_num1 % 2 == 0 or user_num1 % 2 == 0:
    print("One number is an even: True")
else:
    print("One number is an even: False")

# Using "not" to see if a user's numbers are the same, and to see if they picked the unlucky 13 number.
if not user_num1 == user_num2:
    print("Both your numbers are not equal: True")
else:
    print("Both your numbers are not equal: False")

if not user_num1 == 13:
    print("Your number is not unlucky 13: True")
else:
    print("Your number isn't unlucky 13: False")
