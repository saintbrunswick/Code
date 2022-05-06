# Program to sort three integers without usig conditional statments and loops.

import math
import time
import sys
from stat import S_ISREG, ST_CTIME, ST_MODE
import os
import glob
y = int(input("Input first number: "))
x = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)


print("\n")
# Program to sort files by date.a1

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))


print("\n")
# Program to get directory listing, sorted by creation date.

#Relative to absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r"."

#all entries in directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

#regular files, insert creation date
data = ((stat[ST_CTIME], path)
        for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))


print("\n")
# Program to get the details of math module.

#Sets everything to a list of math module.
math_ls = dir(math)
print(math_ls)


print("\n")
# Program to calculate midpoints of a line.

print("\nCalculate the midpoint of a line: ")

x1 = float(input("The value of x (the first endpoint)"))
y1 = float(input("The value of y (the first endpoint)"))

x2 = float(input("The value of x (the first endpoint)"))
y2 = float(input("The value of y (the first endpoint)"))

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print()
print("The midpoint of line is: ")
print("The midpoint's x value is ", x_m_point)
print("The midpoint's y value is ", y_m_point)
print()
