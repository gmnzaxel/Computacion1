# Mensajes generales del juego
WELCOME_MESSAGE = "¡Bienvenido al juego!"
GAME_MENU = "\n--- Menú Principal ---\n1. Atacar\n2. Defenderse\n3. Irse\n4. Menú de Guardado"
SAVE_MENU = "\n--- Menú de Guardado ---\n1. Guardar Progreso\n2. Cargar Progreso\n3. Volver al Menú Principal"
INVALID_OPTION = "Opción no válida. Inténtalo de nuevo."
SAVE_SUCCESS = "Juego guardado exitosamente."
LOAD_SUCCESS = "Progreso cargado exitosamente."
SAVE_FILE_ERROR = "No se encontró ningún archivo de guardado."

# Mensajes de personajes
ATTACK_MESSAGE = "{} atacó a {} causando {} puntos de daño."
TAKE_DAMAGE_MESSAGE = "{}, recibiste {} puntos de daño. Salud restante: {}"
LEVEL_UP_MESSAGE = "{} subió al nivel {}!"

# Narrativa
INTRO_NARRATIVE = """
▒█▀▀█ ░▀░ █▀▀ █▀▀▄ ▀█░█▀ █▀▀ █▀▀▄ ░▀░ █▀▀▄ █▀▀█ 　 █▀▀█
▒█▀▀▄ ▀█▀ █▀▀ █░░█ ░█▄█░ █▀▀ █░░█ ▀█▀ █░░█ █░░█ 　 █▄▄█
▒█▄▄█ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀░ ▀▀▀▀ 　 ▀░░▀

████████╗██╗░░██╗███████╗  ███████╗██╗███╗░░██╗░█████╗░██╗░░░░░
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝██║████╗░██║██╔══██╗██║░░░░░
░░░██║░░░███████║█████╗░░  █████╗░░██║██╔██╗██║███████║██║░░░░░
░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║██║╚████║██╔══██║██║░░░░░
░░░██║░░░██║░░██║███████╗  ██║░░░░░██║██║░╚███║██║░░██║███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝

██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗░█████╗░███╗░░██╗
██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗████╗░██║
██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║██╔██╗██║
██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║██║╚████║
██████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗╚█████╔╝██║░╚███║
╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚══╝

Tu misión es derrotar al malvado Dragón que amenaza con destruir el reino.
Para lograrlo, debes atravesar varias mazmorras llenas de enemigos peligrosos.
Buena suerte y... ¡Que comience la aventura!
"""

#Getters para acceder a los mensajes
def get_welcome_message():
    return WELCOME_MESSAGE

def get_game_menu():
    return GAME_MENU

def get_save_menu():
    return SAVE_MENU

def get_invalid_option():
    return INVALID_OPTION

def get_save_success():
    return SAVE_SUCCESS

def get_load_success():
    return LOAD_SUCCESS

def get_save_file_error():
    return SAVE_FILE_ERROR

def get_attack_message():
    return ATTACK_MESSAGE

def get_take_damage_message():
    return TAKE_DAMAGE_MESSAGE

def get_level_up_message():
    return LEVEL_UP_MESSAGE

def get_intro_narrative():
    return INTRO_NARRATIVE

# Mensajes de poderes especiales
DRAGON_FIRE_MESSAGE = "{} lanzo una llamarada ardiente hacia {} causando {} puntos de daño."
OGRE_SMASH_MESSAGE = "{} realizo un golpe devastador a {} causando {} puntos de daño."

def get_dragon_fire_message():
    return DRAGON_FIRE_MESSAGE

def get_ogre_smash_message():
    return OGRE_SMASH_MESSAGE

# Mensajes de poderes especiales
DRAGON_FIRE_MESSAGE = "{} lanza una llamarada ardiente hacia {} causando {} puntos de daño."
OGRE_SMASH_MESSAGE = "{} realiza un golpe devastador a {} causando {} puntos de daño."
ASSASSIN_MESSAGE = "{} realizó un Golpe Letal y causó {} puntos de daño a {}."
UNDEAD_KNIGHT_MESSAGE = "{} usó su Golpe Maldito y causó {} puntos de daño a {}."
WIZARD_MESSAGE = "{} drenó {} puntos de fuerza de {}."

def get_dragon_fire_message():
    return DRAGON_FIRE_MESSAGE

def get_ogre_smash_message():
    return OGRE_SMASH_MESSAGE

def get_assassin_message():
    return ASSASSIN_MESSAGE

def get_undead_knight_message():
    return UNDEAD_KNIGHT_MESSAGE

def get_wizard_message():
    return WIZARD_MESSAGE
