import dungeon
import constant
import heroes
import save
import json

def main():
    print(constant.INTRO_NARRATIVE)

    # Preguntar al usuario si desea iniciar una nueva partida o cargar una existente
    while True:
        choice = input(constant.NEW_OR_CHARGE).strip().lower()
        
        if choice == 'n':
            # Mostrar los personajes disponibles
            print("Personajes disponibles:")
            print("1. Guerrero")
            print("2. Mago")
            print("3. Arquero")

            # Pedir al jugador que elija un personaje
            while True:
                character_choice = input(constant.ASK_CHARACTER)
                if character_choice in ["1", "2", "3"]:
                    break
                else:
                    print(constant.get_invalid_option())

            # Crear el personaje elegido
            if character_choice == "1":
                player = heroes.Warrior("Guerrero", 160, 50, 20) # Vida, ataque, defensa
            elif character_choice == "2":
                player = heroes.Mage("Mago", 120, 70, 5)
            elif character_choice == "3":
                player = heroes.Archer("Arquero", 140, 52, 10)

            # Crear un objeto Dungeon
            dungeon_game = dungeon.Dungeon(5, 5, player)
            dungeon_game.start_game()

            break  # Salimos del bucle después de iniciar una nueva partida

        elif choice == 'c':
            # Cargar juego existente
            try:
                data = save.load_game()
                player = save.restore_player(data["player"])
                dungeon_game = save.restore_dungeon(data["dungeon"], player)
                print(constant.get_load_success())
            except FileNotFoundError:
                print(constant.get_save_file_error())
                continue  # Volver a preguntar si no se encuentra el archivo
            except json.JSONDecodeError:
                print(constant.FILE_ERROR)
                continue  # Volver a preguntar si hay un error en la carga
            break  # Salimos del bucle después de cargar la partida

        else:
            print(constant.CHARGE_INVALID_OPTION)

    # Aviso para terminar el juego
    print(constant.WARNING)

    # Bucle principal del juego
    while player.get_health() > 0:
        print(constant.get_navigation_menu())
        action = input(constant.ASK_NAVIGATION)
        if action == "w":
            dungeon_game.navigate("norte")
        elif action == "s":
            dungeon_game.navigate("sur")
        elif action == "d":
            dungeon_game.navigate("este")
        elif action == "a":
            dungeon_game.navigate("oeste")
        elif action == "1":  # Opción para guardar/cargar
            # Menú de guardado
            print(constant.get_save_menu())
            save_action = input(constant.ASK_NAVIGATION)
            if save_action == "1":  # Guardar juego
                save.save_game(player, dungeon_game)
                print(constant.get_save_success())
            elif save_action == "2":  # Cancelar
                continue
            else:
                print(constant.get_invalid_option())
        elif action == "ASPIRINE": # Truco aumentar vida
            player.set_health(player.get_health() + 150)
            print(constant.TRICK_HEALTH_INCREASE.format(player.get_health()))

        else:
            print(constant.get_invalid_option())

    if player.get_health() <= 0:
        print(constant.GAME_OVER_MESSAGE)

if __name__ == "__main__":
    main()