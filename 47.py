# Problem 47
# Distinct Primes Factors
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5.
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

def primeOmega(n):
    factors = 0
    x = 2
    while n > 1 and factors < 4:
        if n % x == 0:
            factors += 1
            while n % x == 0:
                n /= x
        x += 1
    return factors > 3

current = 646
run = 0

while True:
    current += 1
    if primeOmega(current):
        run += 1
        if run == 4:
            break
    else:
        run = 0

answer = current - 3

print(answer)

# 134043