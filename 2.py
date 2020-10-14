# Input two numbers and display the larger / smaller number
# 10:01 AM 13-10-2020

a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))

if(a < b): # This line ensures that the value in {a} is always greater than the value in {b}
    a,b = b,a

print(f"Larger number - {str(a)}")
print(f"Smaller number - {str(b)}")