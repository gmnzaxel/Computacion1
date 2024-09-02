# from generator
# from narratives
from characters import Warrior, Mage, Archer
from dungeon import Dungeon  
import save # Importa el sistema de guardado

def game_menu(player, dungeon):
    while True:
        print("\n--- Menú Principal ---")
        print("1. Atacar")
        print("2. Defenderse")
        print("3. Irse")
        print("4. Menú de Guardado")
        option = input("Elige una opción: ")

        if option == '1':
            player.__attack(dungeon.__current_enemy)
        elif option == '2':
            player.__defend(dungeon.__current_enemy)
        elif option == '3':
            print(f"{player.__name} decidió irse.")
            break
        elif option == '4':
            save_menu(player)
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def save_menu(player):
    while True:
        print("\n--- Menú de Guardado ---")
        print("1. Guardar Progreso")
        print("2. Cargar Progreso")
        print("3. Volver al Menú Principal")
        option = input("Elige una opción: ")

        if option == '1':
            save.__save_game(player)
        elif option == '2':
            save.__load_game(player)
        elif option == '3':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def main():
    player = Warrior("Conan", 100, 20, 10)
    dungeon = Dungeon()  

    print("¡Bienvenido al juego!")
    game_menu(player, dungeon)

if _name_ == "_main_":
    main()


