#Problem 4
#Largest Palindrome Product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is: 9009 = 91 × 99
#Find the largest palindrome made from the product of two 3-digit numbers.

digits = 3
end = 10 ** digits - 1
start = 10 ** (digits - 1) - 1
answer = 0

def checkPalindrome(number):
    reverse = 0
    original = number
    
    while number > 0:
        reverse = (reverse * 10) + number % 10
        number //= 10
    
    return reverse == original


for x in range (start, end, 11):
    for y in range (start, end, 1):
        if checkPalindrome(x * y):
            answer = max(answer, x*y)

print(answer)

#906609