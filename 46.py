# Problem 46
# Goldbach's Other Conjecture
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2 × 1²
# 15 = 7 + 2 × 2²
# 21 = 3 + 2 × 3²
# 25 = 7 + 2 × 3²
# 27 = 19 + 2 × 2²
# 33 = 31 + 2 × 1²
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def checkPrime(number):
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True

def check(number):
    for i in primes:
        temp = (number - i)/2
        if int(temp**0.5) ** 2 == temp:
            return False
    return True


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

composite = 35

while True:
    composite += 2
    if checkPrime(composite):
        primes.append(composite)
        continue
    if check(composite):
        break

print(composite)

# 5777