# Determine whether a number is a perfect number, an armstrong number or a palindrome
# 10:31 AM 13-10-2020

from functools import reduce
from math import ceil

x = int(input("Enter an integer - "))

def isArmstrong(n):
    sum_ = 0
    for d in str(n):
        sum_ += int(d)**3
    if(sum_ == n): return True
    else: return False

def isPalindrome(n):
    n = str(n)
    if(n == n[::-1]): return True
    else: return False

def isPerfect(n):
    divisors = getDivisors(n)
    if(reduce(lambda a,v: a+v, divisors) == n): return True
    else: return False

def getDivisors(n):
    # Returns all divisors excluding the number itself
    divisors = [1]
    for i in range(2, n):
        if(n % i == 0):
            divisors.append(i)
    return divisors

if(isArmstrong(x)): print(f"{x} is an armstrong number.")
if(isPalindrome(x)): print(f"{x} is a palindrome.")
if(isPerfect(x)): print(f"{x} is an perfect number.")