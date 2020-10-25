# Count and display the number of vowels, consonants, uppercase, lowercase characters in string.
# 5:28 PM 13-10-2020
# Twice as fast compared to 13.py

x = input("Enter a string...\n")

vowels = consonants = uppercase = lowercase = 0

for character in x:
    if character.isupper: uppercase += 1
    if character.islower: lowercase += 1
    if character.lower() in 'aeiou': vowels += 1
    if character.lower() in 'bcdfghjklmnpqrstvwxyz': consonants += 1

print(f"Vowles - {vowels}")
print(f"Consonants - {consonants}")
print(f"Uppercase - {uppercase}")
print(f"Lowercase - {lowercase}")