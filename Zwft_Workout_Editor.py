# Import necessary libraries
import time
import random

# Define global variables
ftp = int(input('Your FTP is needed to calculate the Power in the format of Zwift.\nYour FTP: '))

watt_mult = float(1/int(ftp))# Multiplier to convert watts to Zwift's format
watt_mult = round(watt_mult,8)
overall_time = 0  # Total time spent in all workout intervals
newlines = []  # List to store additional workout file information

# Get user input for author, workout name, and tag
author = input("Enter the author's name: ")
name = input("Enter the workout name: ")
sport_type = "bike"  # Default sport type
tag = input("Enter a tag for the workout: ")

# Get user input for seconds inclusion
include_seconds = input("Do you want to include seconds in the workout intervals? (y/n) ")

# Define workout intervals list
workout_lines = []

# Loop to add workout intervals
while True:
    add_interval = input("Do you want to add a new interval to your training? (y/n) ")

    # Add new interval
    if add_interval == "y":
        try:
            minutes = int(input("Enter the number of minutes: "))
            overall_time += minutes
        except ValueError:
            minutes = int(input("Enter the number of minutes: "))

        if include_seconds == "y":
            seconds = int(input("Enter the number of seconds: "))
        else:
            seconds = 0

        try:
            cadence = int(input("Enter the cadence: "))
        except ValueError:
            cadence = int(input("Enter the cadence: "))

        try:
            watt = int(input("Enter the power in watts: "))
        except ValueError:
            watt = int(input("Enter the power in watts: "))

        message = input("Enter a message for the interval: ")

        # Calculate total interval time
        time = (minutes * 60) + seconds

        # Convert power to Zwift's format
        powr = watt * watt_mult
        power = round(powr, 8)

        # Add interval information to workout_lines list
        workout_lines.append(
            '<SteadyState Duration="'
            + str(time)
            + '" Power="'
            + str(power)
            + '" pace="0" Cadence="'
            + str(cadence)
            + '">'
        )
        workout_lines.append('<textevent timeoffset="0" message="' + str(message) + '"/>')
        workout_lines.append("</SteadyState>")

    # Exit loop if no more intervals are desired
    if add_interval == "n":
        workout_lines.append('</workout>')
        workout_lines.append('</workout_file>')
        break

# Generate workout file header
head_lines = [
    "<workout_file>",
    '<author>' + str(author) + "</author>",
    '<name>' + str(name) + "</name>",
    "<description></description>",
    '<sportType>' + str(sport_type) + "</sportType>",
    "<tags>",
    '<tag name="' + str(tag) + '"/>',
    "</tags>",
    "<workout>",
]

# Print workout file to disk
with open(name + ".zwo", "w") as f:
    for line in head_lines:
        f.write(line)
        f.write("\n")

    for line in workout_lines:
        f.write(line)
        f.write("\n")

    f.close()

# Display total workout time and closing message
print("Total workout time: " + str(overall_time))
print("Ride on!")
