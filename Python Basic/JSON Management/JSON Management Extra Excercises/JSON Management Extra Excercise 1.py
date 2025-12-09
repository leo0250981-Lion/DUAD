import json

def display_pokemon_data(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        pokemons = json.load(file)

    print("\n=== POKEMON LIST ===")
    for pokemon in pokemons:
        name = pokemon["name"]["english"]
        p_type = ", ".join(pokemon["type"])
        level = pokemon["base"]["HP"]  # Example: Using HP as "level"
        print(f"Name: {name} | Type: {p_type} | Level: {level}")

display_pokemon_data("pokemons.json")