# Input a list of numbers and swap elements at the even location with the elements at the odd location.
# 6:07 PM 13-10-2020

x = eval(input("Enter a list...\n"))

if(type(x) is not list):
    exit("Input provided is not of type list")

lenx = len(x)
for i in range(0, lenx - 1, 2):
    x[i],x[i+1] = x[i+1],x[i]

print(x)