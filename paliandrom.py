text = input("Enter a string: ")
cleaned = text.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
