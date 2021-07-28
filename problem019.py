"""
Project Euler
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# Functions
def check_leap_year(year):
    if year % 4 == 0 and year % 400 != 0:
        return True
    else:
        return False

# Main
# 01/jan/1901 was a Tuesday
# First Sunday was 06/jan/1901

date = [6, 1, 1901]

sum_sundays = 0

while date[2] < 2001:
    date[0] += 7

    if (date[1] == 4 or date[1] == 6 or date[1] == 7 or date[1] == 11) and date[0] > 30:
        date[0] -= 30
        date[1] += 1
    elif date[1] == 2 and date[0] > 28:
        leap = check_leap_year(date[2])
        if leap and date[0] == 29:
            pass
        elif leap:
            date[0] -= 29
            date[1] += 1
        else:
            date[0] -= 28
            date[1] += 1
    elif date[1] == 12 and date[0] > 31:
        date[0] -= 31
        date[1] = 1
        date[2] += 1
    elif date[0] > 31:
        date[0] -= 31
        date[1] += 1


    if date[0] == 1:
        sum_sundays += 1

print(sum_sundays-1)



