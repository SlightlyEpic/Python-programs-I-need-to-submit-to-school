# Compute the greatest common divisor and least common multiple of two integers
# 12:41 AM 13-10-2020

from functools import reduce

a = int(input("Enter first number - "))
b = int(input("Enter second number - "))

def getDivisors(n):
    # Returns all divisors including the number itself
    divisors = [1]
    for i in range(2, n+1):
        if(n % i == 0):
            divisors.append(i)
    return divisors

divA = getDivisors(a)
divB = getDivisors(b)

commonDivisors = set(divA).intersection(divB)

gcd = reduce(lambda a,g: a*g, commonDivisors)
lcm = (a*b)//gcd

print(f"Greatest common divisor = {gcd}")
print(f"Least common multiple = {lcm}")