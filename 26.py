# Problem 26
# Reciprocal Cycles
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 1/2 = 0.5
# 1/3 = 0.(3)
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.1(6)
# 1/7 = 0.(142857)
# 1/8 = 0.125
# 1/9 = 0.(1)
# 1/10 = 0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

d = 1000
current = 0

def decimal(n):
    result = [[0, 10]]
    remainder = 10
    i = 0
    while True:
        i += 1
        quotient = remainder // n
        remainder = remainder % n * 10
        if remainder == 0 or i > 10000:
            return False
        if [quotient, remainder] in result:
            break
        else:
            result.append([quotient, remainder])
    return len(result) - result.index([quotient, remainder])

for i in range(1, d):
    if decimal(i) > current:
        answer = i
        current = decimal(i)

print(answer)

# 983