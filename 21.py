# Problem 21
# Amicable Numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

import itertools

amicableNumbers = []
max = 10000

def checkAmicable(n):
    a = 0
    b = 0
    for number in factorise(n):
        a += number
    if a == n:
        return False
    for number in factorise(a):
        b += number
    if b == n:
        return True
    else:
        return False
    

def factorise(number):
    original = number
    primeFactors = []
    
    while True:
        if number % 2 == 0:
            primeFactors.append(2)
            number /= 2
        else:
            break
    
    for i in range(3, int(original), 2):
        while True:
            if number % i == 0:
                primeFactors.append(i)
                number /= i
            else:
                break
        if number < i:
            break
    
    factors = []
    for i in range(len(primeFactors) + 1):
        for item in list(itertools.combinations(primeFactors, i)):
            product = 1
            for number in item:
                product *= number
            factors.append(product)
    factors = list(dict.fromkeys(factors))
    try:
        factors.remove(original)
    except ValueError:
        pass
    return factors

for i in range(2, max):
    if i not in amicableNumbers:
        if checkAmicable(i):
            amicableNumbers.append(i)

answer = 0

for number in amicableNumbers:
    answer += number

print(answer)

# 31626