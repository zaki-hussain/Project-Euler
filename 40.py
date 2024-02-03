# Problem 40
# Champernowne's Constant
# An irrational decimal fraction is created by concatenating the positive integers: 
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

product = 1
intervals = [1]

for i in range(1,7):
    x = 10 ** i
    intervals.append(int(0.9 * x * i + intervals[i - 1]))

def check(d):
    a = 0
    while d > intervals[a]:
        a += 1
    b = intervals[a - 1]
    c = str(10**(a-1) + ((d - b) // a))[(d - b) % a]
    print(c)
    return int(c)


for i in range(1, 7):
    d = 10 ** i
    product *= check(d)

print(product)

# 210