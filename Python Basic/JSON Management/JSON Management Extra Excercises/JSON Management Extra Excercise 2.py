import json

def search_pokemon_by_type(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        pokemons = json.load(file)

    user_type = input("Enter the Pokémon type you want to search (Water, Fire, Electric, etc.): ").capitalize()

    print(f"\nPokémon of type '{user_type}':")
    found = False
    
    for pokemon in pokemons:
        if user_type in pokemon["type"]:
            print(pokemon["name"]["english"])
            found = True

    if not found:
        print("No Pokémon found with that type.")

search_pokemon_by_type("pokemons.json")