# Empty list to store the entered words
words = []

# Ask the user to enter 5 words
for i in range(5):
    user_word = input("Enter a word: ")
    words.append(user_word)

# Create a new list for words with more than 4 letters
filtered_words = []

for word in words:
    if len(word) > 4:
        filtered_words.append(word)

print(filtered_words)