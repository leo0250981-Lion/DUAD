import csv

file_name = "videogames.csv"  # CSV file name

try:
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        # Skip header row (Name, Genre, Developer, Rating)
        next(reader)

        for row in reader:
            print(f"Name: {row[0]}")
            print(f"Genre: {row[1]}")
            print(f"Developer: {row[2]}")
            print(f"Rating: {row[3]}")
            print()  # Blank line for readability

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except Exception as e:
    print("Unexpected error:", e)