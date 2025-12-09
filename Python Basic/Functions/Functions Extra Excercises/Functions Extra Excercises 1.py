def count_character(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

# Example
text = "programming"
char = "o"

result = count_character(text, char)
print(f"The character appears {result} times")