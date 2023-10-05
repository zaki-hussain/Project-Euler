#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2.
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#m(m+n)=500
#500 = 2^2 × 5^3, so:
m = 20
n = 5

#a = m * n
#b = (m**2 - n**2) / 2
#c = (m**2 + n**2) / 2

answer = 2 * m * n * (m**4 - n**4)

print(answer)

#31875000