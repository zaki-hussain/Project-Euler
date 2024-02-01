# Problem 38
# Pandigital Multiples
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product 192 of and (1, 2, 3).
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1, 2, 3, 4, 5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1, 2, ..., n) where n > 1?

i = 1
answer = 0

def pandigital(all):
    if len(all) != 9:
        return False
    for _ in "123456789":
        if _ not in all:
            return False
    return True

while True:
    n = 1
    concatenatedProduct = []
    while True:
        for digit in str(i * n):
            concatenatedProduct.append(digit)
        if len(concatenatedProduct) < 9:
            n += 1
        else:
            break

    if pandigital(concatenatedProduct):
        answer = max(answer, int("".join(concatenatedProduct)))
    
    if i < 10000:
        i += 1
    else:
        break

print(answer)

# 932718654