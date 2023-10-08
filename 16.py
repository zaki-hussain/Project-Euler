# Problem 16
# Power Digit Sum
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

exponent = 1000
answer = 0
stringResult = str(2 ** exponent)

for number in stringResult:
    answer += int(number)

print(answer)

# 1366