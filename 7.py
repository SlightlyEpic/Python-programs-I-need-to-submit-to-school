# Write a program to input the value of x and n and print the sum of the following series
# x + (x^2)/2 + (x^3)/3 + (x^4)/4 + ... + (x^n)/n
# 10:25 AM 13-10-2020

x = int(input("Enter x - "))
n = int(input("Enter n - "))

sum = 0
for i in range(1, n+1):
    sum += pow(x, i)/i

print(f"Sum of series = {str(sum)}")