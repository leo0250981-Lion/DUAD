file_name = "log.txt"  # The file that will store the text

# Ask the user for a line of text
text = input("Enter a line of text: ")

# Open in append mode "a" (creates file if it doesn't exist)
with open(file_name, "a", encoding="utf-8") as file:
    file.write(text + "\n")

print("The text has been added to the end of the file without erasing previous content.")