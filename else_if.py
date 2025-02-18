'''
Directions:
Accept a numeric grade from the user and display a letter grade. The  grading scale is 
90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F

Check to see if the number given is between 0 and 100.  
'''

# Gets the user to input their numeric grade and converts it to an integer.
user_grade = int(input("Enter your numeric grade: "))

# An integer above 100 will print out this message.
if user_grade > 100:
    print("Numeric grade not within the range of 0 - 100")
# All the logic behind the grading scale, uses less than or equal to print the correct letter grade.
elif user_grade >= 90:
    print("Letter Grade: A")
elif user_grade >= 80:
    print("Letter Grade: B")
elif user_grade >= 70:
    print("Letter Grade: C")
elif user_grade >= 60:
    print("Letter Grade: D")
# Anything above 0 and up to 59 is considered an F.
elif user_grade > 0:
    print("Letter Grade: F")
# A negative integer will print out this message.
else:
    print("Numeric grade not within the range of 0 - 100")
