import dungeon
# import characters
# import item
import constant
import heroes
import save


def main():
    print(constant.INTRO_NARRATIVE)

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
    dungeon_game = dungeon.Dungeon(5, 5)

    # Iniciar el juego
    dungeon_game.start_game()

    # juego
    while True:
        print(constant.get_navigation_menu())
        action = input("¿Qué deseas hacer? ")
        if action == "1":
            dungeon_game.navigate("norte")
        elif action == "2":
            dungeon_game.navigate("sur")
        elif action == "3":
            dungeon_game.navigate("este")
        elif action == "4":
            dungeon_game.navigate("oeste")
        elif action == "5":
            save_action = input("¿Qué deseas hacer? ")
            print("1. Guardar progreso")
            print("2. Cargar progreso")
            if save_action == "1":
                save.save_game(player, dungeon_game)  # Guardar progreso
                print(constant.get_save_success())
            elif save_action == "2":
                data = save.load_game()  # Cargar progreso
                print(constant.get_load_success())
                
                # restaura datos del jugador
                player = save.restore_player(data["player"])
                dungeon_game = save.restore_dungeon(data["dungeon"])
            elif save_action == "3":
                continue  # Volver al menú principal
        else:
            print(constant.get_invalid_option())

# Verificar si el jugador ha encontrado un enemigo
        if dungeon_game.get_enemy_found():
            print(constant.get_enemy_menu())
            enemy_action = input("¿Qué deseas hacer? ")
            if enemy_action == "1":
                # Atacar al enemigo
                dungeon_game.attack_enemy()
            elif enemy_action == "2":
                # Defenderse del enemigo
                dungeon_game.defend_against_enemy()
            elif enemy_action == "3":
                # Irse del enemigo
                dungeon_game.flee_from_enemy()
            else:
                print(constant.get_invalid_option())
            dungeon_game.set_enemy_found(False)

if __name__ == "__main__":
    main()
