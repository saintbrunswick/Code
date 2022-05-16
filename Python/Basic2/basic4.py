# Program to print Unicode charachters.
str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0069\u0073\u0065\u0073 \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
print()
print(str)
print()


print("\n")
# Program to prove that two string variables of same value point same memory location.

str1 = "Python"
str2 = "Python"

print("\nMemory location of str1 = ", hex(id(str1)))
print("Memory location of str2 = ", hex(id(str2)))
print()


print("\n")
# Program to prove that two string variables of same value point same memory location.


def remove_duplicates(nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i-1]
    return len(nums)


print(remove_duplicates([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4]))
print(remove_duplicates([1, 2, 2, 3, 4, 4]))


print("\n")
# Program to create a bytearray from a list.

print()
numbers = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(numbers)
for x in values:
    print(x)
print()


print("\n")
# Program to display a floating number in specified numbers.

order_amt = 212.374
print("\nThe total order amount comes to %f" % order_amt)
print("The total order amount comes to %.2f" % order_amt)
print()
