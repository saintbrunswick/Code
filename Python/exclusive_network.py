# ExclusiveNetwork
# logical operators and compound conditions

print("\tExclusive Computer Network")
print("\t\tMembers only!\n")

security = 0

username = ""
while not username:
    username = input("Username: ")

password = ""
while not password:
    password = input("Password: ")

if username == "Mike Tyson" and password == "boks":
    print("Hi Mike.")
    security = 5
elif username == "Marry Jane" and password == "420":
    print("Hey Marry Jane.")
    security = 3
elif username == "Black" and password == "street":
    print("Nice to see you Mr.Black.")
    security = 3
elif username == "Guest" and password == "guest":
    print("Hi Guest.")
    security = 1
else:
    print("Login failed. You're not so exclusive.\n")

input("\nPress the enter key to exit.")



