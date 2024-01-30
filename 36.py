# Problem 36
# Double-base Palindromes
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

sum = 0

for i in range (1000000):
    if str(i) == str(i)[::-1] and str(bin(i))[2:] == str(bin(i))[2:][::-1]:
        sum += i

print(sum)

# 872187