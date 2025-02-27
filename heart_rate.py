"""
    Objective:
Create a Python script to track heart rate readings and calculate the average heart rate.
Requirements:
Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").
Use a loop to prompt the user for heart rate (in BPM) at each time slot.
Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.
Calculate the average heart rate and display it.
"""

# Variables

time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []
total = 0

# Getting info from the user
for time in time_slots:
    user_bpm = float(
        input(f"Please enter the heart rate (in BPM) for the {time}: "))
    heart_rates.append([time, user_bpm])

# Calculating the average and displaying
for item in range(len(heart_rates)):
    total += heart_rates[item][1]

average = total / len(heart_rates)
print(f"Average heart rate for today: {average:,.2f} BPM")
