# Program to print to stderr.


from __future__ import print_function
import getpass
import os
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


eprint("abc", "efg", "xyz", sep="--")


print("\n")
# Program to acces enviroment variables.

# Acces all environment variables
print("*---------------------------*")
print(os.environ)
print("*---------------------------*")
# Acces a particular environment variable
print(os.environ["HOME"])
print("*---------------------------*")
print(os.environ["PATH"])
print("*---------------------------*")


print("\n")
# Program to get current user name.

print(getpass.getuser())
