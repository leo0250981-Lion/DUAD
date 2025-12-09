import csv

file_name = "videogames.csv"  # CSV file name

try:
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        developer_search = input("Enter the name of the developer to search: ").strip()

        result_found = False
        print(f"\nVideo games developed by {developer_search}:\n")

        for row in reader:
            name = row[0]
            genre = row[1]
            developer = row[2]
            rating = row[3]

            if developer.lower() == developer_search.lower():
                result_found = True
                print(f"- {name} (Rating: {rating}, Genre: {genre})")

        if not result_found:
            print("No games found for that developer.")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except Exception as e:
    print("Unexpected error:", e)