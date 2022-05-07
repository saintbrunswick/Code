# Program to get the size of an object in bytes.
import os
import sys
str1 = "one"
str2 = "four"
str3 = "three"
print()
print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1)) + " bytes")
print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2)) + " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3)) + " bytes")
print()


print("\n")
# Program to get the current value of the recursion limit.

print()
print("Current value of the recursion limit: ")
print(sys.getrecursionlimit())
print()


print("\n")
# Program to concanate N string.

list_of_colors = ["Red", "White", "Black"]
colors = "-".join(list_of_colors)
print()
print("All Colors: "+colors)
print()


print("\n")
# Program to calculate the sum over a container.

s = sum([10, 20, 30])
print("\nSum fo container: ", s)
print()


print("\n")
# Program to test wheter all numbers of a list is greater than certain number.

num = [2, 3, 4]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()


print("\n")
# Program to count the number of occurance of a specific character in string.

s = "The quick brow fox jumps over the lazy dog."
print()
print(s.count("q"))
print()


print("\n")
# Program to chceck wheter a file path is a file or directory.

path = "test.txt"
if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is a file")
else:
    print("\nIt is a special file (socket, FIFO, device file)")
print()
