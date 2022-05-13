# Program to print current call stack.

from http.client import HTTPConnection
import socket
import os
import time
import traceback
print()
def f1(): return abc()
def abc(): traceback.print_stack()


f1()
print()


print("\n")
# Program to get system time.

print()
print(time.ctime())
print()


print("\n")
# Program to clear screen or terminal.

# for windows
# os.system('cls')
#os.system("ls")
#time.sleep(2)

# Ubuntu
#os.system("clear")


print("/n")
# Program to get the name of the host on which routine is running.

host_name = socket.gethostname()
print()
print("Host name: ", host_name)
print()


print("\n")
# Program to access and print a URL;s content to the console.

conn = HTTPConnection("example.com")
conn.request("GET", "/")
result = conn.getresponse()
# retrives the entire contents.
contents = result.read()
print(contents)
