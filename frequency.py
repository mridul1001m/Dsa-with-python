from collections import Counter
text = input("Enter a string: ")
freq = Counter(text)
for char, count in freq.items():
    print(f"'{char}': {count}")
