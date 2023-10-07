# Problem 14
# Longest Collatz Sequence
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

stop = 1000000
most = 0
answer = 0

def nextTerm(n):
    try:
        return test[n]
    except KeyError:
        if n % 2 == 0:
            return int(n / 2)
        else:
            return 3 * n + 1

test = {}

for i in range(2, stop):
    total = 1
    n = i
    while True:
        n = nextTerm(n)
        total += 1
        if n == 1:
            break

    if total > most:
        answer = i
        most = total

print(answer)

# 837799