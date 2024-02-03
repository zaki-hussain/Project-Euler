# Problem 42
# Coded Triangle Numbers
# The nth term of the sequence of triangle numbers is given by, tn = 1/2 n (n + 1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word. If the word value is a triangle number than we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

with open("0042_words.txt", "r") as f:
    words = f.read().replace("\"", "").split(",")

triangles = list(map(lambda x: int(x * (x + 1) / 2), range(1, 27)))

def check(word):
    total = 0
    for letter in word:
        total += ord(letter) - 64
    return total

sum = 0

for word in words:
    sum += check(word) in triangles

print(sum)

# 162