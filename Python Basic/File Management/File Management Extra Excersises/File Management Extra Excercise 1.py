# Input and output file names
input_file = "input.txt"
output_file = "output.txt"

# Open the file and read lines
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Remove newline characters and join into one line
one_line_text = " ".join(line.strip() for line in lines)

# Write the content into a new file
with open(output_file, "w", encoding="utf-8") as file:
    file.write(one_line_text)

print("Content processed successfully.")
print("Final result:", one_line_text)