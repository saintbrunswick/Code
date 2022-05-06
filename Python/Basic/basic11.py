# Program to find local IP addresses using Python stdib.

import time
import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                    if not ip.startswith("127.")][:1], [[(s.connect(("8.8.8.8", 53)),
                                                          s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                                                                                                                 socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


print("\n")
# Program to get height and the width of console window.


def terminal_size():
    import fcntl
    import termios
    import struct
    th, tw, hp, wp = struct.unpack("HHHH",
                                   fcntl.ioctl(0, termios.TIOCGWINSZ,
                                               struct.pack("HHHH", 0, 0, 0, 0)))
    return tw, th


print("Number of colums and rows: ", terminal_size())


print("\n")
# Program to execution time (in seconds) for a Python method.


def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1, n+1):
        s = s + i
    end_time = time.time()
    return s, end_time-start_time


n = 5
print("\nTime to sum of 1 to ", n,
      " and required time to calculate is: ", sum_of_n_numbers(n))


print("\n")
# Time to sum of 1 to 5 and required time to calculate is : (15,2.384185791015629e-06)

n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print(sum_num)
