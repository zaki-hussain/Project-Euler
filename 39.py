# Problem 39
# Integer Right Triangles
# If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, there are exactly three solutions for p = 120.
# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}
# For which value of p ≤ 1000, is the number of solutions maximised?

counts = [0] * 1000
a = 1

while a < 500:
    b = 1
    while b < a:
        c = (a**2 + b**2)**0.5
        p = a + b + c
        if p > 1000:
            break
        if c.is_integer():
            counts[int(p) - 1] += 1
        b += 1
    a += 1
    
print(counts.index(max(counts)) + 1)

# 840