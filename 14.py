# Input a string and determine whether it is a palindrome or not; convert the case of characters in a string
# 5:55 PM 13-10-2020

x = input("Enter a string...\n")

if(x == x[::-1]): print(f"'{x}' is a palindrome'")
else: print(f"'{x}' is not a palindrome'")

print("Inverted case: ")
print(x.swapcase())