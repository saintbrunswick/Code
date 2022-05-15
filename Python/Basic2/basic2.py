# Program to divide a path on the extension separator.

import time
import os.path
for path in ["test.txt", "filename", "/home/stasiek/Documents/GitHub/Code/Python/Basic2/test.txt", "/", ""]:
    print("'%s' :" % path, os.path.splitext(path))


print("\n")
# Program to retrive file properties.


print("File         :", __file__)
print("Access time  :", time.ctime(os.path.getatime(__file__)))
print("Modified time:", time.ctime(os.path.getmtime(__file__)))
print("Change time  :", time.ctime(os.path.getctime(__file__)))
print("Size         :", os.path.getsize(__file__))


print("\n")
# Program to find path refers to a file directory when you encounter a path name.

for file in [__file__, os.path.dirname(__file__), "/", "./broken_link"]:
    print("File         :", file)
    print("Absolute     :", os.path.isabs(file))
    print("Is File?     :", os.path.isfile(file))
    print("Is Dir?      :", os.path.isdir(file))
    print("Is Link?     :", os.path.islink(file))
    print("Exists       :", os.path.exists(file))
    print("Link Exists? :", os.path.lexists(file))


print("\n")
# Program to check if a number is positive, negative or zero.

num = float(input("Input a number: "))
if num > 0:
    print("It is a positive number.")
elif num == 0:
    print("It is Zero.")
else:
    print("It is a negative number.")


print("\n")
# Program to get numbers divisible by 15 from a list using an anonymous function.

num_list = [45, 55, 60, 37, 100, 105, 220]
# uses anonymous funcion to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are: ", result)
