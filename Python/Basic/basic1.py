# Display the current date and TimeoutError
from math import pi
import datetime
now = datetime.datetime.now()
print("Current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


print("\n")
# Accept the radius of a circle from user and compute the area
r = float(input("Input the radius of the circle:"))
print("The are of the circle with radius " + str(r) + " is: " + str(pi * r**2))
