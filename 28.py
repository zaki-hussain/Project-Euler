# Problem 28
# Number Spiral Diagonals
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

width = 1001
diagonal = int((width + 1) / 2)

def powerTwo(n):
    return 16 * int(n * (n + 1) * (2 * n + 1) / 6)

def powerOne(n):
    return 28 * int(n * (n + 1) / 2)

def powerZero(n):
    return 16 * n - 3

answer = powerTwo(diagonal) - powerOne(diagonal) + powerZero(diagonal)

print(answer)

# 669171001