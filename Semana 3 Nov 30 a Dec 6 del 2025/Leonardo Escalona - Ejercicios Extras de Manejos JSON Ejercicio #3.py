import json

def show_pokemon_stats(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        pokemons = json.load(file)

    print("\n=== POKEMON STATS ===")
    for pokemon in pokemons:
        name = pokemon["name"]["english"]
        attack = pokemon["base"]["Attack"]
        defense = pokemon["base"]["Defense"]
        speed = pokemon["base"]["Speed"]

        print(f"\nName: {name}")
        print(f"Attack: {attack}")
        print(f"Defense: {defense}")
        print(f"Speed: {speed}")

show_pokemon_stats("pokemons.json")