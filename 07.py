# Problem 7
# 10001st Prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

import math

max = 10001
prime = 1
current = 2

def checkPrime(number):
    maxDivisor = math.ceil(math.sqrt(number)) + 1
    if number % 2 == 0:
        return False
    for divisor in range (3, maxDivisor, 2):
        if number % divisor == 0:
            return False
    return True

while prime < max:
    current += 1
    if checkPrime(current):
        prime += 1

print(current)

# 104743