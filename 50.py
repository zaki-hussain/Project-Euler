# Problem 50
# Consecutive Prime Sum
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13.
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def checkPrime(number):
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True

primes = [2]
count = 0
total = 2
current = 0
answer = 0
target = 1000000

for i in range(3, 10000, 2):
    if checkPrime(i):
        primes.append(i)
        total += i
        count += 1

for i in range(count):
    total -= primes[i]
    a = total
    b = count - i
    while a > 0 and (a > target or a % 2 == 0 or not(checkPrime(a))):
        a -= primes[i + b]
        b -= 1
    if b > current and a > 0:
        current = b
        answer = a

print(answer)
# 997651