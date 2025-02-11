'''
    Requirements:
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
'''

# Users enter numerical values and are stored in various variables. Used in the calculation section.
budget = float(input("Please enter your net monthly income for the budget: "))
housing = float(input(
    "Please enter your housing costs (rent or mortgage plus HOA if you have it): "))
utilities = float(input("Please enter your monthly utilities costs: "))
groceries = float(input("Please enter your monthly groceries costs: "))
transportation = float(
    input("Please enter your monthly transportation costs: "))
health_care = float(input("Please enter your monthly health care costs: "))
personal_care = float(input("Please enter your monthly personal care costs: "))
clothing = float(input("Please enter your monthly clothing costs: "))
debt = float(input("Please enter your monthly debt payments: "))

# All calculations for budget percent spent in each category, how much remains, and how much in total was spent.
housing_percent = housing/budget * 100
utilities_percent = utilities/budget * 100
groceries_percent = groceries/budget * 100
transportation_percent = transportation/budget * 100
health_care_percent = health_care/budget * 100
personal_care_percent = personal_care/budget * 100
clothing_percent = clothing/budget * 100
debt_percent = debt/budget * 100

total_costs = (housing+utilities+groceries+transportation +
               health_care+personal_care+clothing+debt)
remaining_money = budget - total_costs

# The percent spent of the budget in each category is displayed, as well as both the remaining budget and how much of it was spent.
print(f"\nYour housing is %{housing_percent:.1f} of your monthly budget")
print(f"Your utilities is %{utilities_percent:.1f} of your monthly budget")
print(f"Your groceries is %{groceries_percent:.1f} of your monthly budget")
print(f"Your transportation is %{
      transportation_percent:.1f} of your monthly budget")
print(f"Your health care is %{health_care_percent:.1f} of your monthly budget")
print(f"Your personal care is %{
      personal_care_percent:.1f} of your monthly budget")
print(f"Your clothing is %{clothing_percent:.1f} of your monthly budget")
print(f"Your debt is %{debt_percent:.1f} of your monthly budget")

print(f"\nYou spent a total of ${total_costs:.1f}, and have ${
      remaining_money} of your budget remaining.")
