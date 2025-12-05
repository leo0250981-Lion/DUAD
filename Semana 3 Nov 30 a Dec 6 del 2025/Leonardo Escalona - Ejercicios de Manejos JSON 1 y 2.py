import json

def add_pokemon(json_file):
    try:
        # 1️⃣ Read existing JSON File
        with open(json_file, "r", encoding="utf-8") as file:
            pokemons = json.load(file)

        # 2️⃣ Get new Pokémon information
        print("\n=== ADD NEW POKÉMON ===")
        name = input("Pokémon Name: ")
        types = input("Types (comma separated if more than one, e.g., Fire, Flying): ").split(",")

        # Clean spaces
        types = [t.strip() for t in types]

        print("--- ENTER BASE STATS ---")
        hp = int(input("HP: "))
        attack = int(input("Attack: "))
        defense = int(input("Defense: "))
        sp_attack = int(input("Sp. Attack: "))
        sp_defense = int(input("Sp. Defense: "))
        speed = int(input("Speed: "))

        # 3️⃣ Create Pokémon dictionary
        new_pokemon = {
            "name": {"english": name},
            "type": types,
            "base": {
                "HP": hp,
                "Attack": attack,
                "Defense": defense,
                "Sp. Attack": sp_attack,
                "Sp. Defense": sp_defense,
                "Speed": speed
            }
        }

        # 4️⃣ Add to the list
        pokemons.append(new_pokemon)

        # 5️⃣ Save updated JSON
        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(pokemons, file, indent=2)

        print("\nPokémon successfully added 👍")

    except FileNotFoundError:
        print("Error: JSON file not found.")

    except ValueError:
        print("Error: You must enter numeric values for stats.")

    except Exception as e:
        print("An error has occurred:", e)


# Run function
add_pokemon("pokemons.json")  # Change the filename if yours has a different name