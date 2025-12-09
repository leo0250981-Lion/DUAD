import csv

file_name = "videogames.csv"  # CSV file name

try:
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        genre_count = {}

        for row in reader:
            genre = row[1].strip()  # Genre column
            
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1

        print("\nGenres found:\n")
        for genre, count in genre_count.items():
            print(f"{genre}: {count}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except Exception as e:
    print("Unexpected error:", e)