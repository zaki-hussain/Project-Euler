# Problem 33
# Digit Cancelling Fractions
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from fractions import Fraction

all = Fraction(1/1)

def check(numerator, denominator):
    nStr = str(numerator)
    dStr = str(denominator)
    if nStr[0] in dStr:
        if numerator / denominator == int(nStr[1]) / int(dStr.replace(nStr[0], "", 1)):
            return True
    if nStr[1] in dStr:
        if numerator / denominator == int(nStr[0]) / int(dStr.replace(nStr[1], "", 1)):
            return True


for denominator in range (12, 100):
    if denominator % 10 != 0:
        for numerator in range (11, denominator):
            if numerator % 10 != 0:
                if check(numerator, denominator):
                    all *= Fraction(numerator, denominator)

print(all.denominator)

# 100