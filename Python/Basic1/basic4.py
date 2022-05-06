# Program to get the volume of a sphere with radius 6.
pi = 3.1415926535897931
r = 6.0
v = 4.0/3.0*pi*r**3
print("The volume of sphere is: ", v)


print("\n")
# Program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.


def difference(n):
    if n < 17:
        return 17-n
    else:
        return(n-17)*2


print(difference(22))
print(difference(14))


print("\n")
# Program to test where a number is with 100 of 1000 or 2000.


def near_thousand(n):
    return((abs(1000-n) <= 100) or (abs(2000-n) <= 100))


print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))


print("\n")
# Program to display the first and last color from list

color_list = ["Red", "Green", "White", "Black"]
print("%s %s" % (color_list[0], color_list[-1]))
