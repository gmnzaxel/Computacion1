import main
import heroes
import dungeon
import json

def save_game(player, dungeon_game):
    data = {
        "player": {
            "name": player.get_name(),
            "health": player.get_health(),
            "defense": player.get_defense(),
            # Otros atributos del jugador
        },
        "dungeon": {
            "position": dungeon_game.get_current_position(),
            # Otros atributos del dungeon
        }
    }
    with open('save_file.json', 'w') as save_file:
        json.dump(data, save_file)


def load_game():
    with open('save_file.json', 'r') as save_file:
        data = json.load(save_file)
    return data


def restore_player(player_data):
    # recrear jugador
    if player_data["name"] == "Guerrero":
        return heroes.Warrior(player_data["name"], player_data["health"], 15, player_data["defense"])
    elif player_data["name"] == "Mago":
        return heroes.Mage(player_data["name"], player_data["health"], 10, player_data["defense"])
    elif player_data["name"] == "Arquero":
        return heroes.Archer(player_data["name"], player_data["health"], 12, player_data["defense"])


def restore_dungeon(dungeon_data):
    # restaurar la mazmorra con datos cargados
    dungeon_game = dungeon.Dungeon(10, 10)
    dungeon_game.set_position(dungeon_data["position"]) 
    return dungeon_game