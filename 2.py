#Problem 2
#Even Fibonacci Numbers
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

maxNumber = 4000000

fibn2 = 2
fibn1 = 8
total = 2
while fibn2 < maxNumber and fibn1 < maxNumber:
    temp = 4 * fibn1 + fibn2
    fibn2, fibn1 = fibn1, temp
    total += fibn2

print(total)

#4613732