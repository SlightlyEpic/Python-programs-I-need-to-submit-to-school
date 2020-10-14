# Input a list/tuple of elements, search for a given element in the list/tuple.
# 6:13 PM 13-10-2020

x = eval(input("Enter a list/tuple...\n"))
n = input("Enter word to search for...\n")

typeofx = type(x)
if(typeofx is not list and typeofx is not tuple):
    exit("Input provided is not of type list/tuple")

try:
    index = x.index(n)
except ValueError:
    print(f"Could not find '{n}' in the sequence")
else:
    print(f"Found '{n}' in sequence at index {index}")