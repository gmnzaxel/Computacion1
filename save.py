import pickle  # Puedes usar pickle para serializar y deserializar objetos

def save_game(player):
    with open("savefile.sav", "wb") as save_file:
        pickle.dump(player, save_file)
    print("Juego guardado exitosamente.")

def load_game(player):
    try:
        with open("savefile.sav", "rb") as save_file:
            loaded_player = pickle.load(save_file)
            player.name = loaded_player.name
            player.health = loaded_player.health
            player.strength = loaded_player.strength
            player.defense = loaded_player.defense
            print("Juego cargado exitosamente.")
    except FileNotFoundError:
        print("No se encontró ningún archivo de guardado.")