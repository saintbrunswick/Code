# Program to display your details like name, age, address in three different lines.

import os
import platform
import struct
import os.path
import math


def personal_details():
    name, age = "Simon", 22
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))


personal_details()


print("\n")
# Program to solve (x + y) * (x + y).

x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))


print("\n")
# Program to compute the future value of a specified principal amount, rate of interest, and nmber of years.

amt = 10000
int = 3.5
years = 7

future_value = amt*((1+(0.01*int)) ** years)


print("\n")
# Program to compute the distance between the points (x1, y1) and (x2, y2).

p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

print(distance)


print("\n")
# Program to check whether a file exists.

open("abc.txt", "w")
print(os.path.isfile("abc.txt"))


print("\n")
# Program to determine whether a Python shell is executing in 32bit or 64bit mode on OS.

# For 32bit will return 32 and for 64bit will return 64.
print(struct.calcsize("P") * 8)


print("\n")
# Program to get OS name, platform and release info.

print(os.name)
print(platform.system())
print(platform.release())
