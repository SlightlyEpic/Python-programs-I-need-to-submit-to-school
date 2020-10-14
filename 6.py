# Write a program to input the value of x and n and print the sum of the following series
# 1 - x + x^2 - x^3 + x^4 + ... + x^n
# 10:24 AM 13-10-2020

x = int(input("Enter x - "))
n = int(input("Enter n - "))

sum = 0
for i in range(0, n+1):
    sum += pow(-x, i)

print(f"Sum of series = {str(sum)}")