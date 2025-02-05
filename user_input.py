"""_summary_
    Getting user input

    Design a Python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
        Housing (rent or mortgage)
        Utilities
        Groceries
        Transportation
        Health Care
        Personal Care
        Clothing
        Debt
        Calculate the percentage of the total budget spent in each category.
        Display the results in a user-friendly format using f-strings.
        Ensure your code is well-commented to explain the functionality of different sections.
"""

first_name = input("Please enter your first name: ")
print(f"Hello {first_name}")
# preferred way to convert to an int
age = int(input("How old are you? (Use numerals)  "))
# age = int(age)
new_age = age + 1
print(f"Next year you will be {new_age}. ")
print("You will be " + str(new_age) + " next year.")
print("_" * 50)
