# Program to get system command output.

import subprocess
# file and directory listing.
returned_text = subprocess.check_output(
    "dir", shell=True, universal_newlines=True)
print("dir command to list file directory")
print(returned_text)


print("\n")
# Programs
