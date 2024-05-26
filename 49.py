# Prime Permutations
# Problem 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

def checkPrime(number):
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return number

def checkPermutations(n1, n2, n3):
    n1, n2, n3 = [int(a) for a in str(n1)], [int(a) for a in str(n2)], [int(a) for a in str(n3)]
    n1.sort()
    n2.sort()
    n3.sort()
    return n1 == n2 == n3

difference = 3330

for i in range (10**3 + 1, 10**4 - 2 * difference, 2):
    if checkPrime(i) and checkPrime(i + difference) and checkPrime(i + difference * 2) and checkPermutations(i, i + difference, i + 2 * difference) and i != 1487:
        answer = str(i) + str(i + difference) + str(i + 2 * difference)

print(answer)
# 296962999629