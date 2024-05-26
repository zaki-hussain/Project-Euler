# Problem 48
# Self Powers
# The series, 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.
# Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 10¹⁰⁰⁰.

sum = 0
for i in range(1, 1000):
    sum += i**i % 10**10

answer = sum % 10**10

print(answer)

# 9110846700