"""
    Objective:
Develop a Python-based Madlib based on a song of your choice. The program should collect at least 8 different pieces of information from the user and incorporate them into the song using named arguments. The goal is to practice using functions, user input, and string manipulation in Python.

Important Note:
Choose any song you like for your madlib, but remember, no Rickrolling! Be creative and respectful in your song choice.

Task:
Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content.
Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc.
Write the Function:
Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
Use f-strings to incorporate these parameters into the song's lyrics.
Ensure the function prints the customized song lyrics.
Collect User Input:
Write code to collect user input for each of the 8 variables.
Use clear and descriptive prompts to guide the user.
Call the Function:
Call the custom_song function with the user inputs as named arguments.
Ensure the order of arguments matches the parameters in your function definition.
"""


# The function has 8 parameters
def custom_song(star_adj, star_color, animal, place, feeling, light_adj, sound, dream_adj):
    print(f"\n{star_adj}, {star_adj}, {star_color} star,")
    print("How I wonder what you are!")
    print(f"Up above the {place} so high,")
    print(f"Like a {animal} in the sky.\n")

    print(f"When the {light_adj} night is near,")
    print(f"And I hear a {sound} so clear,")
    print("Then I close my eyes so tight,")
    print(f"Feeling {feeling}, warm, and light.\n")

    print(f"Twinkle on, my {dream_adj} star,")
    print("Guiding me from near and far.")
    print(f"{star_adj}, {star_adj}, {star_color} star,")
    print("How I wonder what you are!")


# Collect all the necessary words from the user
star_adj = input("Enter an adjective to describe a star: ")
star_color = input("Enter a color: ")
animal = input("Enter any animal: ")
place = input("Enter any place: ")
feeling = input("Enter a feeling: ")
light_adj = input("Enter any adjective for night: ")
sound = input("Enter any sound: ")
dream_adj = input("Enter an adjective for dreams: ")

# Calls the song with the user inputs implemented
custom_song(star_adj=star_adj, star_color=star_color, animal=animal, place=place,
            feeling=feeling, light_adj=light_adj, sound=sound, dream_adj=dream_adj)
