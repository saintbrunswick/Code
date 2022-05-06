# Program to calculate the sum of three given numbers, if the values are equal then return thric of their sum.

def sum_thrice(x, y, z):

    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))


print("\n")
# Program to get a string which is n (non-negative integer) copies of given string.


def larger_string(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result


print(larger_string("abc", 2))
print(larger_string(".py", 3))


print("\n")
# Program to get a new string from given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.


def new_string(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str


print(new_string("Array"))
print(new_string("IsEmpty"))


print("\n")
# Program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This number is an odd number.")
else:
    print("This number is even number.")


print("\n")
# Program to count the number 4 in a given list.


def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count


print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))


print("\n")
# Program to get the n (non-negative integer) copies of the firstb two characters of given string. Return the n copies of the whole string if the lenght is less than 2.


def substring_copy(str, n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]

    result = ""
    for i in range(n):
        result = result + substr
    return result


print(substring_copy("abcdef", 2))
print(substring_copy("p", 3))
