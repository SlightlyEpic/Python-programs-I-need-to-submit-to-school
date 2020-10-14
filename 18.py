# Input a list of numbers and test if a number is equal to the sum of the cubes of
# its digits. Find the smallest and largest such number from the given list of numbers
# 7:40 AM 14-10-2020

x = eval(input("Enter a list...\n"))

if(type(x) is not list):
    exit("Input provided is not of type list")

def isArmstrong(n):
    sum_ = 0
    for d in str(n):
        sum_ += int(d)**3
    if(sum_ == n): return True
    else: return False

maximum = minimum = 0

for i in range(0, len(x)):
    current = x[i]
    if(isArmstrong(current)): 
        print(f"{current} is an armstrong number.")
        if(current > maximum): maximum = current
        if(current < minimum): minimum = current

print(f"Largest armstrong number is {maximum}")
print(f"Smallest armstrong number is {minimum}")