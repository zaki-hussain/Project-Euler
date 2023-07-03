#Problem 3
#Largest Prime Factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

import math

number = 600851475143

def checkPrime(dividend):
    maxDivisor = math.ceil(math.sqrt(dividend))
    if dividend % 2 == 0:
        return False
    
    for divisor in range (3, maxDivisor, 2):
        if dividend % divisor == 0:
            return False
    
    return True


for factor in range (3, number, 2):
    if number % factor == 0:
        if checkPrime(number / factor):
            answer = int(number / factor)
            break
        number /= factor

print(answer)

#6857