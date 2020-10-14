# Input three numbers and display the largest / smallest number
# 10:11 AM 13-10-2020

a = int(input("Please enter a number - "))
b = int(input("Please enter a number - "))
c = int(input("Please enter a number - "))

minimum = min(a,b,c)
maximum = max(a,b,c)

print(f"Largest number - {str(maximum)}")
print(f"Smallest number - {str(minimum)}")