import json
from collections import defaultdict

def average_level_by_type(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        pokemons = json.load(file)

    type_levels = defaultdict(list)

    # Group Pokémon by type
    for pokemon in pokemons:
        level = pokemon["base"]["HP"]  # Change here if you use another attribute
        for p_type in pokemon["type"]:
            type_levels[p_type].append(level)

    # Display average per type
    print("\n=== AVERAGE LEVEL BY TYPE ===")
    for p_type, levels in type_levels.items():
        avg = sum(levels) / len(levels)
        print(f"Type: {p_type} → Average Level: {avg:.2f}")

average_level_by_type("pokemons.json")