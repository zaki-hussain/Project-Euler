#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 =3 85.
#The square of the sum of the first ten natural numbers is,
#(1+2+...+10) = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
#3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

max = 100

def sumSquare(max):
    return int(max * (max + 1) * (2 * max +1 ) / 6)

def squareSum(max):
    return int(max * (max + 1) / 2) ** 2

answer = squareSum(max) - sumSquare(max)

print(answer)

#25164150