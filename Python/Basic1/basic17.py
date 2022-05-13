# Program to get ASCII value of character.

import os
print()
print(ord('a'))
print(ord('A'))
print(ord('1'))
print(ord('@'))
print()


print("\n")
# Progra, to get the size of a file.

file_size = os.path.getsize("test.txt")
print("\nThe size of test.txt is: ", file_size, "Bytes.")
print()


print("\n")
# Given variables x=30 and y=20, write a program to pint "30+20=50"

x = 30
y = 20
print("\n%d+%d=%d" % (x, y, x+y))
print()


print("\n")
# Program to perform an action if a cndition is true.

n = 1
if n == 1:
    print("\nFirst day of month")
print()


print("\n")
# Program to create a copy of its own source code.

print()
print((lambda str="print(lambda str=%r: (str %% str))()": (str % str))())
print()


print("\n")
# Program to swap to variables.

a = 30
b = 20
print("\nBefore swap a = %d and b = %d" % (a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" % (a, b))
print()


print("\n")
# Program to define a string containing special characters in various forms.

print()
print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')
print()


print("\n")
# Program to get the idenity of an object.

obj1 = object()
obj1_address = id(object)
print()
print(obj1_address)
print()


print("\n")
# Program to convert a byte string to a list of integers.

x = b'Abc'
print()
print(list(x))
print()


print("\n")
# Program to check wheter a string is numeric.

str = "a123"
#str = "1123"
try:
    i = float(str)
except (ValueError, TypeError):
    print("\nNot numeric")
print()
