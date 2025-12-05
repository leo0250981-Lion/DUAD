import csv

def save_videogames_tsv():
    n = int(input("Enter the number of video games: "))

    with open("videogames.tsv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")
        
        # Write headers
        writer.writerow(["name", "genre", "developer", "esrb_rating"])

        # Enter data
        for _ in range(n):
            name = input("Video game name: ")
            genre = input("Genre: ")
            developer = input("Developer: ")
            rating = input("ESRB Rating: ")
            
            writer.writerow([name, genre, developer, rating])

    print("TSV file successfully saved as videogames.tsv")


save_videogames_tsv()