# Input a number and check if the number if prime or composite number
# 12:30 PM 13-10-2020

x = int(input("Enter an integer - "))

try:
    for i in range(2, x):
        if(x % i == 0): raise StopIteration
    else:
        print(f"{x} is a prime number")
except StopIteration:
    print(f"{x} is a composite number")