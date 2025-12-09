file_name = "text.txt"  # Change this name if your file has a different name

try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

    # Split the content into words separated by spaces and/or newlines
    words = content.split()

    print(f"This file contains {len(words)} words")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except Exception as e:
    print("Unexpected error:", e)