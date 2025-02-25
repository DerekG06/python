"""
Assignment Steps:
Create a list representing 20 seats, numbered 1 to 20.
Display the list of available seats to the customer.
Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.
Remove the selected seat from the list of available seats and display the updated list.
If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
Ensure the program gracefully handles all scenarios and is user-friendly.
"""

# List of items to buy
available_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Shows the initial starting list for the user to see
print("Available seats:", available_seats)

while True:  # This while True will keep the program running until 0 is entered by the user
    seat = int(input("Enter the seat number to purchase (0 to close program): "))

    # Closes the program if the user enters 0
    if seat == 0:
        print("Purchase process ended. Thank you!")
        break  # This break will leave the while True loop and end the program
    else:
        # Sees if the user's seat is in the available_seats list, and removes it if it is
        if seat in available_seats:
            available_seats.remove(seat)
            print(f"Seat {seat} successfully purchased!\n")

        # If a number that isn't in the list no matter what, this will be printed
        else:
            print(
                f"Seat {seat} is invalid or already sold. Please choose a different seat.")

    # Shows the changed list
    print("Updated available seats:", available_seats)
