# Problem 19
# Counting Sundays
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def leapYear(year):
    return 366 if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0 else 365

months = {
    1: 31,
    2: lambda x: 29 if (x % 4 == 0 and not x % 100 == 0) or x % 400 == 0 else 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

day = 1
day += leapYear(1900) % 7
answer = 0

for year in range (1901, 2001):
    for month in range (1,13):
        if day == 0:
            answer += 1
        if not month == 2:
            day = (day + months[month]) % 7
        else:
            day = (day + months[month](year)) % 7

print(answer)

# 171