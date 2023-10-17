# Problem 23
# Non-Abundant Sums
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import itertools
import math

abundantNumbers = []

def checkAbundant(number):
    total = 0
    for item in factorise(number):
        total += item
    if total > number:
        abundantNumbers.append(number)


def factorise(number):
    original = number
    primeFactors = []
    while True:
        if number % 2 == 0:
            primeFactors.append(2)
            number /= 2
        else:
            break
    
    for i in range(3, math.ceil(math.sqrt(number)) + 1  , 2):
        while True:
            if number % i == 0:
                primeFactors.append(i)
                number /= i
            else:
                break
        if i >= number:
            break

    if number > 2:
        primeFactors.append(int(number))
    
    factors = []
    
    for i in range(len(primeFactors)):
        for item in list(itertools.combinations(primeFactors, i)):
            product = 1
            for n in item:
                product *= n
            factors.append(product)
    
    factors = list(dict.fromkeys(factors))

    return factors

for i in range (12, 28124):
    checkAbundant(i)

abundantSums = []

for i in range(len(abundantNumbers)):
    for j in range(i, len(abundantNumbers)):
        result = abundantNumbers[i] + abundantNumbers[j]
        if result > 28123:
            break
        else:
            abundantSums.append(result)

abundantSums = list(dict.fromkeys(abundantSums))

answer = int(28123 * 28124 / 2) - sum(abundantSums)

print(answer)

# 4179871