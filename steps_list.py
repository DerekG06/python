"""
1. Create a List: Start by creating a list named days that includes all seven days of the week.
2. Initialize an Empty List: Create an empty list called steps to store the number of steps taken each day.
3. User Input: Using a loop, ask the user to enter the number of steps they took for each day.
4. Store Steps: Append the user's input to the steps list.
5. Display Daily Steps: Show the user the steps recorded for each day.
6. Total Steps: Calculate and display the total number of steps taken in the week.
7. Average Steps: Calculate and display the average steps.
"""

# My variables and lists
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
steps = []
total = 0

for i in range(len(days)):
    day = days[i]
    user_steps = int(input(f"Enter how many steps you took on {day}: "))
    steps.append([day, user_steps])
# Shows the user the list of daily steps.
print("Starting from Monday, here are your daily steps!:")
print(steps)
print("\n")

# Total amount of steps
for item in range(len(steps)):
    total += steps[item][1]
print(f"Total steps: {total}")

# Average amount of steps
average = total / len(steps)
print(f"Average steps: {average}")
