# Input and output filenames
input_file = "input.txt"
output_file = "output.txt"

# Read original file and write uppercase content
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

with open(output_file, "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line.upper())

print("The content has been successfully converted to uppercase!")