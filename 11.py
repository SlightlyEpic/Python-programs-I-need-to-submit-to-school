# Display the terms of the Fibonacci series
# 12:34 AM 13-10-2020

n = int(input("Enter number of terms to display - "))

i = 1
j = 1

print(i)
print(j)
for r in range(1, n-1):
    currentTerm = i + j
    print(currentTerm)
    i = j
    j = currentTerm