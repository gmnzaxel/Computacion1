import json
import heroes
import dungeon

def save_game(player, dungeon):
    # diccionario con los datos que queremos guardar
    data = {
        "player": {
            "name": player.get_name(),
            "health": player.get_health(),
            "strength": player.get_strength(),
            "defense": player.get_defense(),
            "level": player.get_level(),
            "experience": player.get_experience(),
            "position": player.get_position()
        },
        "dungeon": {
            "visited_positions": list(dungeon.get_visited_positions()),  # Convertir a lista
            "enemies": list(dungeon.get_defeated_enemies()),  # Convertir a lista
            "items": list(dungeon.get_collected_items())  # Convertir a lista
        }
    }
        #Datos guardados en JSON
    with open("save_file.json", "w") as save_file:
        json.dump(data, save_file)

def load_game():
    # Cargar los datos del archivo JSON
    with open("save_file.json", "r") as save_file:
        data = json.load(save_file)
    return data

def restore_player(player_data):
    player = None
    if player_data["name"] == "Guerrero":
        player = heroes.Warrior(player_data["name"], player_data["health"], player_data["strength"], player_data["defense"])
    elif player_data["name"] == "Mago":
        player = heroes.Mage(player_data["name"], player_data["health"], player_data["strength"], player_data["defense"])
    elif player_data["name"] == "Arquero":
        player = heroes.Archer(player_data["name"], player_data["health"], player_data["strength"], player_data["defense"])

    player.set_level(player_data["level"])
    player.set_experience(player_data["experience"])
    player.set_position(tuple(player_data["position"]))
    return player

def restore_dungeon(dungeon_data, player):
    dungeon_instance = dungeon.Dungeon(5, 5, player)

    visited_positions = {tuple(pos) for pos in dungeon_data["visited_positions"]}
    dungeon_instance.set_visited_positions(visited_positions)

    defeated_enemies = set(dungeon_data["enemies"])
    collected_items = set(dungeon_data["items"])

    dungeon_instance.set_defeated_enemies(defeated_enemies)
    dungeon_instance.set_collected_items(collected_items)

    # Llama a generate_level para generar enemigos y objetos
    dungeon_instance.generate_level()

    return dungeon_instance