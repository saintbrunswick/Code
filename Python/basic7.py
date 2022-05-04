# Program to get the least common multiple (LCM) of two positive integers.

def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1

    return lcm


print(lcm(4, 6))
print(lcm(15, 17))


print("\n")
# Program to sum of three given integers. However, if two values are equal sum will be zero.


def sum(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum


print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))


print("\n")
# Program to sum of two given integers. However, if sum is between 15 to 20 it will return 20.


def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum


print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))


print("\n")
# Program which will return true if two given integer values are equal or their sum or difference is 5.


def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False


print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))


print("\n")
# Program to add two objects if both objects are integer type.

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    return a + b

print(add_numbers(10, 20))
