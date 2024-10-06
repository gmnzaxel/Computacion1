import dungeon
# import characters
# import item
import constant
import heroes
import json


def main():
    print(constant.get_welcome_message())

    # Mostrar los personajes disponibles
    print("Personajes disponibles:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")

    # Pedir al jugador que elija un personaje
    character_choice = input("¿Qué personaje deseas elegir? ")

    # Crear el personaje elegido
    if character_choice == "1":
        player = heroes.Warrior("Guerrero", 100, 15, 5)
    elif character_choice == "2":
        player = heroes.Mage("Mago", 80, 10, 5)
    elif character_choice == "3":
        player = heroes.Archer("Arquero", 90, 12, 5)
    else:
        print(constant.get_invalid_option())
        return

    # Crear un objeto Dungeon
    dungeon_game = dungeon.Dungeon(10, 10)

    # Iniciar el juego
    dungeon_game.start_game()

    # Bucle principal del juego
    while True:
        # Mostrar el menú principal
        print(constant.get_game_menu())

        # Pedir al jugador que elija una acción
        action = input("¿Qué deseas hacer? ")

        # Procesar la acción del jugador
        if action == "1":
            # Navegar o atacar
            print("Elige una dirección para navegar: norte, sur, este, oeste")
            direction = input("Dirección: ").lower()
            if direction in ["norte", "sur", "este", "oeste"]:
                dungeon_game.navigate(direction)
            else:
                print(constant.get_invalid_option())
        elif action == "2":
            # Defenderse
            player.set_defense(player.get_defense() + 10)
            print(constant.get_defend_message())
        elif action == "3":
            # Irse
            print(constant.get_flee_message())
            break  # Salir del bucle y terminar el juego
        elif action == "4":
            # Menú de guardado
            print(constant.get_save_menu())
            save_action = input("¿Qué deseas hacer? ")
            if save_action == "1":
                save_game(player, dungeon_game)  # Guardar progreso
                print(constant.get_save_success())
            elif save_action == "2":
                data = load_game()  # Cargar progreso
                print(constant.get_load_success())
                # Aquí es donde deberías restaurar los valores de player y dungeon
                # Basado en los datos cargados
                player = restore_player(data["player"])
                dungeon_game = restore_dungeon(data["dungeon"])
            elif save_action == "3":
                continue  # Volver al menú principal
        else:
            print(constant.get_invalid_option())


def save_game(player, dungeon_game):
    data = {
        "player": {
            "name": player.get_name(),
            "health": player.get_health(),
            "defense": player.get_defense(),
            # Otros atributos del jugador según sea necesario
        },
        "dungeon": {
            "position": dungeon_game.get_current_position(),
            # Otros atributos del dungeon según sea necesario
        }
    }
    with open('save_file.json', 'w') as save_file:
        json.dump(data, save_file)


def load_game():
    with open('save_file.json', 'r') as save_file:
        data = json.load(save_file)
    return data


def restore_player(player_data):
    # Aquí debes recrear el jugador usando los datos cargados
    if player_data["name"] == "Guerrero":
        return heroes.Warrior(player_data["name"], player_data["health"], 15, player_data["defense"])
    elif player_data["name"] == "Mago":
        return heroes.Mage(player_data["name"], player_data["health"], 10, player_data["defense"])
    elif player_data["name"] == "Arquero":
        return heroes.Archer(player_data["name"], player_data["health"], 12, player_data["defense"])


def restore_dungeon(dungeon_data):
    # Aquí puedes restaurar la mazmorra con los datos cargados
    dungeon_game = dungeon.Dungeon(10, 10)
    dungeon_game.set_position(dungeon_data["position"])  # Asumimos que tienes un setter para la posición
    return dungeon_game


if __name__ == "__main__":
    main()
