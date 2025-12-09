def sort_songs(input_file, output_file):
    try:
        # Read the file line by line
        with open(input_file, "r", encoding="utf-8") as file:
            songs = file.readlines()

        # Remove line breaks and sort alphabetically
        songs = [s.strip() for s in songs]
        songs.sort()

        # Save into a new file
        with open(output_file, "w", encoding="utf-8") as file:
            for s in songs:
                file.write(s + "\n")

        print("Songs have been sorted and saved successfully.")

    except FileNotFoundError:
        print("Error: The file does not exist.")