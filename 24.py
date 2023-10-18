# Problem 24
# Lexicographic Permutations
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools

index = 1000000

answerList = list(itertools.permutations(range(10), 10))[index - 1]

answer = 0

for i, j in enumerate(answerList):
    answer += j * 10 ** (9 - i)

print(answer)

# 2783915460