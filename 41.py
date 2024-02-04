# Problem 41
# Pandigital Prime
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

from itertools import permutations
import math

answer = 0

def checkPrime(number):
    if number % 2 == 0:
        return False
    maxDivisor = math.ceil(math.sqrt(number)) + 1
    for divisor in range (3, maxDivisor, 2):
        if number % divisor == 0:
            return False
    return True


for i in range(9, 0, -1):
    for combo in permutations(range(i, 0, -1), i):
        b = int("".join(map(str, combo)))
        if checkPrime(b):
            answer = b
            break
    if answer != 0:
        break

print(answer)

# 7652413