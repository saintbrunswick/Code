# Program to locate Python site-packages.

import cProfile
from os.path import isfile, join
from os import listdir
import multiprocessing
import os
from subprocess import call
import site
print(site.getusersitepackages())


print("\n")
# Program to call an external command in Python.

call(["ls", "-l"])


print("\n")
# Program to get te path and name of the file that is currently ececuting.

print("Current File Name: ", os.path.realpath(__file__))


print("\n")
# Current File Name

print(multiprocessing.cpu_count())


print("\n")
# Program to parse a string to Float or Integer.

n = "246.2458"
print(float(n))
print(int(float(n)))


print("\n")
# Program to list all files in a directory in Python.

file_list = [f for f in listdir("/home/stasiek")
             if isfile(join("/home/stasiek", f))]
print(file_list)


print("\n")
# Program to print without newline or space.

for i in range(0, 10):
    print("*", end="")
print("\n")


print("\n")
# Program to determine profiling of Python programs.


def sum():
    print(1+2)


cProfile.run("sum()")
