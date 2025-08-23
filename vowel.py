
def is_vowel(char):
    return char.lower() in 'aeiou'
text = input("Enter a string: ")
vowels = []
consonants = []
for char in text:
    if char.isalpha(): 
        if is_vowel(char):
            vowels.append(char)
        else:
            consonants.append(char)
print("Vowels in the string:", ' '.join(vowels))
print("Number of vowels:", len(vowels))
print("Consonants in the string:", ' '.join(consonants))
print("Number of consonants:", len(consonants))
