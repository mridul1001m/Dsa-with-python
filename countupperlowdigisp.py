text = input("Enter a string: ")
upper = lower = digits = special = 0
for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digits)
print("Special characters:", special)
