# Problem 1
# Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

number = 999
factor1 = 3
factor2 = 5

def sumOfMultiples(factor):
    x = number // factor
    return x * (x + 1) * factor / 2 

answer = int(sumOfMultiples(factor1) + sumOfMultiples(factor2) - sumOfMultiples(factor1 * factor2))
# Assumes that factor1 and factor2 are prime

print(answer)

# 233168