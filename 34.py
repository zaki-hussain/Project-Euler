# Problem 34
# Digit Factorials
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial
factorials = [factorial(i) for i in range(0, 10)]
total = 0

def check(number):
    sum = 0 
    for digit in str(number):
        sum += factorials[int(digit)]
    if sum == number:
        return True
    
for i in range(3, 10000000):
    if check(i):
        total += i

print(total)

# 40730