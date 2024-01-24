# Problem 32
# Pandigital Products
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a through pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

products = set()

def checkPandigital(all):
    for _ in "123456789":
        if _ not in all:
            return False
    return True

def check(range1, range2, range3, range4):
    for i in range(range1, range2):
        for j in range(range3, range4):
            n = i * j
            if n > 9999:
                break
            if checkPandigital(str(i) + str(j) + str(n)):
                products.add(n)

check(1, 10, 1000, 10000)
check(10, 100, 100, 1000)

print(sum(products))