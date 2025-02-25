"""
Task:
Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.
"""

# List where the names will be stored
names = []

# A loop that will run 5 times to get the 5 names, and will add it to the list and force it to be lower case
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name.lower())

# The Bubble Sort Algorithm process
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            names[i], names[i + 1] = names[i + 1], names[i]
            swapped = True

# This will print the sorted list
print("Sorted List: ")
print(names)

# Reverse the sorted list
names.reverse()

# This will print the reversed list after name.reverse() is ran
print("\nReversed List: ")
print(names)
