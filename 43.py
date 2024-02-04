# Problem 43
# Sub-string Divisibility
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# d2d3d4 = 406
# d3d4d5 = 063
# d4d5d6 = 635
# d5d6d7 = 357
# d6d7d8 = 572
# d7d8d9 = 728
# d8d9d10 = 289

# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations

total = 0

for combo in permutations(range(0, 10), 10):
    a = "".join(map(str, combo))
    if int(a[1:4]) % 2 + int(a[2:5]) % 3 + int(a[3:6]) % 5 + int(a[4:7]) % 7 + int(a[5:8]) % 11 + int(a[6:9]) % 13 + int(a[7:10]) % 17 == 0:
        total += int(a)

print(total)

# 16695334890