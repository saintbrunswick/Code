# Program to test wheter a passed letter is a vowel or not.

def is_vowel(char):
    all_vowels = "aeiou"
    return char in all_vowels


print(is_vowel("c"))
print(is_vowel("e"))


print("\n")
# Program to check wheteher a specified value is contained in a group of values.


def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False


print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))


print("\n")
# Program to create a histogram from a given list of integers.


def histogram(items):
    for n in items:
        output = ""
        times = n
        while(times > 0):
            output += '*'
            times = times - 1
        print(output)


histogram([2, 3, 6, 5])


print("\n")
# Program to concate all elements in a list into a string and return it.


def concatenate_list_data(list):
    result = ""
    for element in list:
        result += str(element)
    return result


print(concatenate_list_data([1, 5, 12, 2]))


print("\n")
# Program to print out a set contain all the colors from color_list_1 wich are not present in color_list_2.

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))


print("\n")
# Program that will accept the base and height of a triangle and compute the area.

b = int(input("Input the base: "))
h = int(input("Input the height: "))

area = b*h/2

print("area = ", area)


print("\n")
# Program to compute the greatest common divisor (GCD) of two positive integers.


def gcd(x, y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd


print(gcd(12, 17))
print(gcd(4, 6))
