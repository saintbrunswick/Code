# Program to calculate the hypotenuse of right angled triangle.

from math import sqrt
print("Input lengths of shorter triangle sides: ")
a = float(input("a: "))
b = float(input("b: "))

c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is ", c)


print("\n")
# Program to covert the distance (in feet) to inches, yards, and miles.

d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in inches is %.2f yards." % d_yards)
print("The distance in inches is %.2f miles." % d_miles)


print("\n")
# Program to convert all units of time into seconds.

days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds

print("The amounts of seconds ", time)


print("\n")
# Program to get an absolute file path.


def absolute_file_path(path_fname):
    import os
    return os.path.abspath("path_fname")


print("Absolute file path: ", absolute_file_path("test.txt"))
