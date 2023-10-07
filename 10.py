# Problem 10
# Summation of Primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

max = 2000000
sum = 2

def checkPrime(number):
    maxDivisor = math.ceil(math.sqrt(number)) + 1
    for divisor in range (3, maxDivisor, 2):
        if number % divisor == 0:
            return False
    return True

for i in range (3,max,2):
    if checkPrime(i):
        sum += i

print(sum)

# 142913828922