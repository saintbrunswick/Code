#Program to display the examination schedule (extract the date from exam_sr_date)
from datetime import date
import calendar
exam_st_date = (11, 12, 2022)
print("The examination will start from: %i / %i / %i" % exam_st_date)

print("/n")
# Program that accepts integer(n) and compute the value of n+nn+nnn.
a = int(input("Input an integer: "))
n1 = int("%s" % (a))
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
print(n1+n2+n3)

print("/n")
# Program to print the document(syntax, description etc.) of Python build in function(s).
print(abs.__doc__)

print("/n")
# Program to print the calendar of a given month and year.
y = int(input("Input the year: "))
m = int(input("Input the month: "))
print(calendar.month(y, m))

print("/n")

# Display formated text
print("""
a string that you "don't" have to escape
This
is a ......... multi-line
heredoc string ------> example
""")

print("\n")
# Program to calculate number fo days between two dates.
f_date = date(2022, 4, 23)
l_date = date(2022, 12, 24)
delta = l_date - f_date
print(delta.days)
