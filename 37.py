# Problem 37
# Truncatable Primes
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math
primes = (1, 2, 3, 5, 7)

truncPrimes = set()
count = 0

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

def addDigit(number):
    global sum
    global count
    for prime in primes:
        joined = str(prime)+str(number)
        for x in range(len(joined)):
            a = int(joined[:(x+1)])
            valid = True
            if not checkPrime(int(joined[:(x+1)])):
                valid = False
                break
        if valid:
            truncPrimes.add(int(joined))
            count += 1
            addDigit(joined)
        


for prime in primes:
    for prime in primes:
        addDigit(prime)

print(truncPrimes, count)
print(len(truncPrimes))