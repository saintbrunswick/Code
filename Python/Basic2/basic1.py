# Program to get system command output.

import os
import subprocess
# file and directory listing.
returned_text = subprocess.check_output(
    "dir", shell=True, universal_newlines=True)
print("dir command to list file directory")
print(returned_text)


print("\n")
# Program to extract the file name from a given path.

print()
print(os.path.basename("/home/stasiek/Documents/GitHub/Code/Python/Basic2/basic1.py"))
print()


print("\n")
# Program to get effective group id, effective user id, real group id, a list of supplemental group ids assosiated with the current process.
print("\nEffective group id: ", os.getegid())
print("Effective user id: ", os.geteuid())
print("Real group id: ", os.getgid())
print("List of supplemental group ids: ", os.getgroups())
print()


print("\n")
# Program to get users environment.

print()
print(os.environ)
print()
