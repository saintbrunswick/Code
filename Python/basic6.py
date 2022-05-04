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
