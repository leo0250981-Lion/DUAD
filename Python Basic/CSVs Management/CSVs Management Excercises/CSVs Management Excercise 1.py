import csv

def save_videogames_csv():
    n = int(input("Enter the number of video games: "))

    with open("videogames.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Write headers
        writer.writerow(["name", "genre", "developer", "esrb_rating"])

        # Enter data
        for _ in range(n):
            name = input("Video game name: ")
            genre = input("Genre: ")
            developer = input("Developer: ")
            rating = input("ESRB Rating: ")
            
            writer.writerow([name, genre, developer, rating])

    print("CSV file successfully saved as videogames.csv")


save_videogames_csv()