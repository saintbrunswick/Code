# Accept name and surname as input and print it in reverse order
fname = input("Type your first name: ")
sname = input("Type your surname: ")
print("Nice to meet you " + sname + " " + fname)

# python 2.x
# y = raw_input("Your message")

# python 3.x
# y = input("Your message")


print("/n")
# Accept a seqence of cmma-separated numbers from user and generate a list and a tuple with those numbers.
values = input("Input some comma separated numbers: ")
list = values.split(",")
tuple = tuple(list)
print("List : ", list)
print("Tuple : ", tuple)

print("/n")
# Accept a file name from user and print the extension of that.
filename = input("Input the Filename: ")
f_extens = filename.split(".")
print("The extension of the file is: " + repr(f_extens[-1]))

print("/n")
# Program to display the first and last color from the fallowing list
# color_list = ["Red","Green","White","Black"]
color_list = ["Red", "Green", "White", "Black"]
print("%s %s" % (color_list[0], color_list[-1]))
