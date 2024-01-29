# Problem 35
# Circular Primes
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import math

sum = 13

def checkPrime(number):
    if number % 2 == 0:
        return False
    maxDivisor = math.ceil(math.sqrt(number)) + 1
    for divisor in range (3, maxDivisor, 2):
        if number % divisor == 0:
            return False
    return True


def check(number):
    nStr = str(number)

    for x in range(len(nStr)):
        if not checkPrime(int(nStr[x:] + nStr[:x])):
            return False

    return True
        

for i in range (100, 1000000):
    sum += check(i)
        
print(sum)

# 55