# Find the largest/smallest number in a list/tuple
# 6:00 PM 13-10-2020

x = eval(input("Enter a list/tuple...\n"))

typeofx = type(x)
if(typeofx is not list and typeofx is not tuple):
    exit("Input provided is not of type list/tuple")

max_ = max(x)
min_ = min(x)

print(f"Maximum = {max_}")
print(f"Minimum = {min_}")