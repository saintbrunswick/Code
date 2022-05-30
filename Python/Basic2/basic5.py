# Program to display a floating number in specified number.

order_amt = 212.374
print("\nThe total order amount comes to %f" % order_amt)
print("The total order amount comes to %.2f" % order_amt)
print()


print("\n")
# Program to format a cpecified string to limit the number of characters to 6.

str_num = "1234567890"
print()
print("%.6s" % str_num)
print()


print("\n")
# Program to determinate wheter variable is defined or not.

try:
    x = 1
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")
try:
    y
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")


print("\n")
# Program to empty a variable without destroing it.

n = 20
d = {"x": 200}
l = [1, 3, 5]
t = (5, 7, 8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())


print("\n")
# Program to wheter multiple variables have the same value.

a = 20
b = 20
c = 20
if a == b == c == 20:
    print("All variables have same value!")
