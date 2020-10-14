# Write a program to input the value of x and n and print the sum of the following series
# x + (x^2)/2! - (x^3)/3! + (x^4)/4! + ... + (x^n)/n
# 10:27 AM 13-10-2020

from math import factorial

x = int(input("Enter x - "))
n = int(input("Enter n - "))

sum = 0
for i in range(2, n+1): # Computes (x^2)/2! - (x^3)/3! + (x^4)/4! + ... + (x^n)/n
    sum += pow(-x, i)/factorial(i)
sum += x # Adds the remaining +x to the sum

print(f"Sum of series = {str(sum)}")