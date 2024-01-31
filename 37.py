# Problem 37
# Truncatable Primes
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math

def checkPrime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    maxDivisor = math.ceil(math.sqrt(number)) + 1
    for divisor in range (3, maxDivisor, 2):
        if number % divisor == 0:
            return False
    return True

def check(number):
    n = str(number)
    for x in range(len(n)):
        if not (checkPrime(int(n[:(x+1)])) and checkPrime(int(n[x:]))):
            return False
    return True

sum = 0
count = 0
i = 11

while count < 11:
    if check(i):
        sum += i
        count += 1
    i += 1

print(sum)

# 748317