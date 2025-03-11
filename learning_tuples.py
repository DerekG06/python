"""
Create a tuple named programming_classes with these classes: 'Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals'.
Write a program that uses a for loop to print each class in the tuple.
Use the len function to print how many courses are in the tuple.
Make sure to use a main function for this program.
Try this out, and you'll understand how tuples work in Python well!
"""


def main():
    # programming_classes is the tuple
    programming_classes = ("Intro to Python", "Advanced Python", "Database Essentials",
                           "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")

    print("Programming Certificate Classes:")
    for course in programming_classes:  # Will print out index 0 to 5
        print(course)

    # Prints the total number of classes by using the len() method
    print(f"\nTotal number of courses: {len(programming_classes)}")


main()
