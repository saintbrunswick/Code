# Accept name and surname as input and print it in reverse order
fname = input("Type your first name: ")
sname = input("Type your surname: ")
print("Nice to meet you " + sname + " " + fname)

# python 2.x
# y = raw_input("Your message")

# python 3.x
# y = input("Your message")


# Accept a seqence of cmma-separated numbers from user and generate a list and a tuple with those numbers.
values = input("Input some comma separated numbers: ")
list = values.split(",")
tuple = tuple(list)
print("List : ",list)
print("Tuple : ",tuple)
