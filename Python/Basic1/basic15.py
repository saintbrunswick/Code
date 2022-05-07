# Program to hash a word.

import textwrap
import sys
soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2,
           4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]

word = input("Input the word to be hashed: ")

word = word.upper()

coded = word[0]

for a in word[1:len(word)]:
    i = 65-ord(a)
    coded = coded+str(soundex[i])
print()
print("The code word is: "+coded)
print()


print("\n")
# Program to get the copyright information.

print("\nPython Copyright Information")
print(sys.copyright)
print()


print("\n")
# Program to get the command-line arguments (name of script, the number of arguments, arguments) passed to script.

print("This is the name/path of the script: "), sys.argv[0]
print("Number of arguments: ", len(sys.argv))
print("Argument list: ", str(sys.argv))


print("\n")
# Program to test wheter the system is a big-endian platform or little-endian platform.

print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()


print("\n")
# Program to find the avaible built-in modules.

module_name = ", ".join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))
