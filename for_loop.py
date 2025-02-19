'''
Write a Python program to find and print all numbers divisible by 7 between 1 and 300.
Use a for loop and the modulus operator (%).
'''

# For loop, it starts at 1 and goes up until 300, in increments of 1 to make sure all numbers are checked.
for i in range(1, 300):
    if i % 7 == 0:
        # If a number has no remainder when divided, it gets printed out in the terminal.
        print(i)
    elif i % 7 != 0:
        # If a number has a remainder, it skips it and starts over with the next number.
        continue
