import csv

file_name = "videogames.csv"  # CSV file name

try:
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        # Ask user for ESRB rating
        rating_filter = input("Enter the ESRB rating to search (E, T, M, etc.): ").strip()

        print(f"\nGames with ESRB rating '{rating_filter}':\n")

        found = False
        for row in reader:
            if row[3].strip().upper() == rating_filter.upper():
                found = True
                print(f"Name: {row[0]}")
                print(f"Genre: {row[1]}")
                print(f"Developer: {row[2]}")
                print(f"Rating: {row[3]}")
                print()

        if not found:
            print("No games found with that rating.")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except Exception as e:
    print("Unexpected error:", e)