# Program to locate Python site-packages.

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
# Program
