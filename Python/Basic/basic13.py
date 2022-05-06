# Program to get file creation and modification date/time.

import os.path
import time
print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))


print("\n")
# Program to conver seconds to day, hour, minutes and second.

time = float(input("Input time in second: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


print("\n")
# Program to calculate body mass index.

height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilograms: "))
print("Your body mass index is: ", round(weight / (height * height), 2))


print("\n")
# Program to convert pressure in kilopascals to pounds per square inch, a milimiter of mercury (mmHg) and atmosphere pressure.

kpa = float(input("Input pressure in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: %.2f psi" % (psi))
print("The pressure in milimeters of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))


print("\n")
# Program to calculate the sum of the digits in an integer.

num = int(input("Input a four digit numbers: "))
x = num//1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num-x*1000 - x1*100 - x2*10
print("The sum of digits in number is ", x+x1+x2+x3)
