# Problem 5
# Smallest Multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

largest = 20

# Note: this will only work if the largest number is under 27 as it doesn't cosider cube numbers, except for 8

answer = 2

def checkPrime(number):
    maxDivisor = math.ceil(math.sqrt(number)) + 1
    if number % 2 == 0:
        return False
    for divisor in range (3, maxDivisor, 2):
        if number % divisor == 0:
            return False
    return True

for i in range (3,largest+1):
    if checkPrime(i):
       answer *=i
    elif math.sqrt(i) % 1 == 0:
        answer *= int(math.sqrt(i))

print(answer)

# 232792560