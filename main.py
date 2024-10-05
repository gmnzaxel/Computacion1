import dungeon
import characters
import item
import constant
import heroes

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
            # Atacar
            dungeon_game.navigate("norte")
        elif action == "2":
            # Defenderse
            player.set_defense(player.get_defense() + 10)
            print(constant.get_defend_message())
        elif action == "3":
            # Irse
            print(constant.get_flee_message())
        elif action == "4":
            # Menú de guardado
            print(constant.get_save_menu())
            save_action = input("¿Qué deseas hacer? ")
            if save_action == "1":
                # Guardar progreso
                print(constant.get_save_success())
            elif save_action == "2":
                # Cargar progreso
                print(constant.get_load_success())
            elif save_action == "3":
                # Volver al menú principal
                continue
        else:
            print(constant.get_invalid_option())

if __name__ == "__main__":
    main()