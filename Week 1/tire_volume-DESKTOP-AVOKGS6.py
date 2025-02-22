# My assignment exceeds expectations because I followed all the requirements on 
# the rubric and also added the additional feature of a prompt that asks for
# the phone number.

import math
from datetime import datetime

tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
volume = (math.pi * tire_width * tire_width * aspect_ratio *((tire_width * aspect_ratio) + (2540 * wheel_diameter)))/10000000000
print(f"The approximate volume is {volume:.2f} liters")

# Call the now() method to get the current date and time as a datetime object from the computer's operating system.
current_date_and_time = datetime.now()
# Use an f-string to print only the date part of the current date and time.
# print(f"{current_date_and_time:%Y-%m-%d}")

current_date_and_time = datetime.now()

with open("volumes.txt", mode="at") as volumes:
    print(f"{current_date_and_time:%Y-%m-%d}, {tire_width}, {aspect_ratio}, {wheel_diameter}, {volume:.2f}", file = volumes)

user_purchase = input("Would you like to buy tires with these dimensions? (yes/no) ")

while user_purchase.lower() != "yes" and user_purchase.lower() != "no":
    user_purchase = input("Would you like to buy tires with these dimensions? (yes/no) ")

if user_purchase.lower() == "yes":
    phone_number = input("What is your phone number? ")
        
    with open("volumes.txt", mode="at") as volumes:
        print(f"{phone_number}", file = volumes)
