text = input("Enter the text: ")
words = text.split()
longest_word = max(words, key=len)
print("The longest word is:", longest_word)
