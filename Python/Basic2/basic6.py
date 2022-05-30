# Program to sum of all counts in a collection.

from math import sqrt
from inspect import getmodule
import collections
num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
print(sum(collections.Counter(num).values()))


print("\n")
# Program to get the actual module object for a given object.

print(getmodule(sqrt))


print("\n")
# Program to check whether an integer fits in 64 bit.

int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())
