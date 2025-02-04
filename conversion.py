'''
    Create a Python program that converts kilograms to pounds. 
    Use at least four different samples to convert. 
    A sample of the math is provided below; do not use the same 
    example in your program.

    Kilograms to Pounds Conversion:
    To convert kilograms (kg) to pounds (lb), use the formula:

    Pounds (lb) = Kilograms (kg) * 2.20462

    Example: 5 kg * 2.20462 = 11.0231 lb

'''

# First conversion, and variables are named "kilo_#"", "pounds_#"", and "c"
c = 2.20462

kilo_1 = 150
pounds_1 = kilo_1 * c

# print statements, and "{pounds_#:.1f}" allows 1 decimal place
print(f"{kilo_1} kilograms = {pounds_1:.1f} pounds")

# Second conversion
kilo_2 = 75
pounds_2 = kilo_2 * c

print(f"{kilo_2} kilograms = {pounds_2:.1f} pounds")

# Third conversion
kilo_3 = 100
pounds_3 = kilo_3 * c

print(f"{kilo_3} kilograms = {pounds_3:.1f} pounds")

# Fourth conversion
kilo_4 = 125
pounds_4 = kilo_4 * c

print(f"{kilo_4} kilograms = {pounds_4:.1f} pounds")
