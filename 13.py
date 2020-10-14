# Count and display the number of vowels, consonants, uppercase, lowercase characters in string.
# 5:28 PM 13-10-2020

from re import findall,IGNORECASE

x = input("Enter a string...\n")

vowels = len(findall("[aeiou]", x, flags=IGNORECASE))
consonants = len(findall("[^aeiou \d]", x, flags=IGNORECASE))
uppercase = len(findall("[A-Z]", x))
lowercase = len(findall("[a-z]", x))

print(f"Vowles - {vowels}")
print(f"Consonants - {consonants}")
print(f"Uppercase - {uppercase}")
print(f"Lowercase - {lowercase}")