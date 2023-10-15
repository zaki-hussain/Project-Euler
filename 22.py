# Problem 22
# Names Scores
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 11 + 9 + 14, is the 983th name in the list. So, COLIN would obtain a score of 983 × 53 = 49714.
# What is the total of all the name scores in the file?

import string

letters = {b: a + 1 for a, b in enumerate(string.ascii_uppercase)}

fileName = "0022_names.txt"

with open(fileName, "r") as f:
    names = f.read().split(",")

names.sort()

total = 0

for i, name in enumerate(names):
    alphabeticalValue = 0
    for letter in name[1:-1]:
        alphabeticalValue += letters[letter]
    total += (i + 1) * alphabeticalValue

print(total)