# Problem 17
# Number Letter Counts
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 20 contains letters. The use of "and" when writing out numbers is in compliance with British usage.

total = 0

words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

def convert(integer):
    if integer in words:
        return len(words[integer])
    elif integer < 100:
        first = len(words[int(str(integer)[0]) * 10])
        second = len(words[int(str(integer)[-1])])
        return first + second
    else:
        hundreds = len(words[int(str(integer)[0])] + "hundred")
        rest = int(str(integer)[-2:])
        if rest == 0:
            return hundreds
        elif rest in words:
            return hundreds + len("and") + len(words[rest])
        else:
            first = len(words[int(str(integer)[1]) * 10])
            second = len(words[int(str(integer)[-1])])
            return hundreds + len("and") + first + second

for i in range (1,1000):
    total += convert(i)

total += len("onethousand")

print(total)

# 21124