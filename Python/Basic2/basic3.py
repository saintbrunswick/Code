# Program to make file lists from current directory using a wildcard.

from functools import reduce
import glob
file_list = glob.glob("*.*")
print(file_list)


print("\n")
# Program to remove the first item from a specified list.

color = ["Red", "Black", "Green", "White", "Orange"]
print("\nOrginal Color: ", color)
del color[0]
print("After removing the first color: ", color)
print()


print("\n")
# Program to input a number, if it is not a number generate an error message.

while True:
    try:
        a = int(input("input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()


print("\n")
# Program to filter the positive numbers from a list.

nums = [34, 1, 0, -23]
print("Orginal numbers in the list: ", nums)
new_nums = list(filter(lambda x: x > 0, nums))
print("Positive numbers in the list: ", new_nums)


print("\n")
# Proram to compute the product of a list of integers (without usin a loop).

numbers = [10, 20, 30, ]
numbers_product = reduce((lambda x, y: x * y), numbers)
print("Product of the numbers: ", numbers_product)
