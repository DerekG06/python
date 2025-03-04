"""
    Requirements:
Global Variables:
Conversion constants for weight (1 lb = 0.453592 kg) and height (1 in = 0.0254 m).
Main Function:
Prompt the user for their weight in pounds and height in inches.
Convert the inputs to metric units using global conversion constants.
Calculate BMI using the formula bmi = weight / (height * height).
Determine the BMI category based on standard ranges.
Display the BMI value and category.
Commenting:
Include comments to explain key parts of the code.
"""


# Global conversion constants, will never change
LB_TO_KG = 0.453592  # WEIGHT: 1 pound = 0.453592 kilograms
IN_TO_M = 0.0254     # HEIGHT: 1 inch = 0.0254 meters


def main():
    # The user will enter their weight and height in inches and pounds.
    weight_lb = int(input("Enter your weight in pounds: "))
    height_in = int(input("Enter your height in inches: "))

    # The user's weight and height are converted to KG, using the global constants and multiplying them.
    weight_kg = weight_lb * LB_TO_KG
    height_m = height_in * IN_TO_M

    # BMI formula is used to find user's BMI.
    bmi = weight_kg / (height_m * height_m)

    # Using standard ranges for BMI the if, elif, and else are used to find what category the user lands.
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal weight"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    # Displays the user's BMI, and based the category of the variable "category" will be shown.
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")


main()
