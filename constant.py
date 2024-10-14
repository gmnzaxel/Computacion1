# Mensajes generales del juego
WELCOME_MESSAGE = "¡Bienvenido al juego!"
GAME_MENU = "\n--- Menú Principal ---\n1. Atacar\n2. Defenderse\n3. Irse\n4. Menú de Guardado"
SAVE_MENU = "\n--- Menú de Guardado ---\n1. Guardar Progreso\n2. Cargar Progreso\n3. Volver al Menú Principal"
INVALID_OPTION = "Opción no válida. Inténtalo de nuevo."
SAVE_SUCCESS = "Juego guardado exitosamente."
LOAD_SUCCESS = "Progreso cargado exitosamente."
SAVE_FILE_ERROR = "No se encontró ningún archivo de guardado."
GAME_OVER_MESSAGE = "¡Juego terminado! Gracias por jugar."
NAVIGATION_MENU = "\n--- Menú de Navegación ---\n1. Norte\n2. Sur\n3. Este\n4. Oeste\n5. Menú de Guardado"


# Mensajes de personajes
ATTACK_MESSAGE = "{} atacó a {} causando {} puntos de daño."
TAKE_DAMAGE_MESSAGE = "{}, recibiste {} puntos de daño. Salud restante: {}"
LEVEL_UP_MESSAGE = "{} subió al nivel {}!"
GAIN_EXPERIENCE_MESSAGE = "{} ganó {} puntos de experiencia."
STRENGTH_DECREASE_ITEM_MESSAGE = "{} ha perdido {} puntos de fuerza"
DEFENSE_DECREASE_ITEM_MESSAGE = "{} ha perdido {} puntos de defensa"
SHIELD_DECREASE_ITEM_MESSAGE = "{} ha perdido {} puntos de escudo"
DAMAGE_ITEM_MESSAGE = "{} ha recibido {} puntos de daño"

#Getters para acceder a los mensajes
def get_navigation_menu():
    return NAVIGATION_MENU

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

def get_gain_experience_message():
    return GAIN_EXPERIENCE_MESSAGE

def get_defend_message():
    return "El personaje se defiende"

def get_flee_message():
    return "El personaje huye"

# Mensajes de poderes especiales
DRAGON_FIRE_MESSAGE = "{} lanzo una llamarada ardiente hacia {} causando {} puntos de daño."
OGRE_SMASH_MESSAGE = "{} realizo un golpe devastador a {} causando {} puntos de daño."

def get_dragon_fire_message():
    return DRAGON_FIRE_MESSAGE

def get_ogre_smash_message():
    return OGRE_SMASH_MESSAGE

# Mensajes enemigos
ENEMY_ATTACK_MESSAGE = "{} ataca a {} y causa {} de daño."
ENEMY_DEFEATED_MESSAGE = "{} ha sido derrotado."
ENEMY_RESURRECTED_MESSAGE = "{} ha sido resucitado con {} puntos de salud."
ENEMY_BLEED_EFFECT_MESSAGE = "{} ha sido afectado por un efecto de sangrado."
ENEMY_EVASION_MESSAGE = "{} ha esquivado el ataque."
ENEMY_ANGRY_MESSAGE = "{} se ha enfurecido y su fuerza ha aumentado a {}."
ENEMY_MAGIC_SHIELD_MESSAGE = "{} ha activado un escudo mágico."
ENEMY_TAKE_DAMAGE_MESSAGE = "{} ha recibido {} de daño y ahora tiene {} de salud."
ENEMY_TREASURE_MESSAGE = "{} ha dejado un tesoro."

DRAGON_FIRE_MESSAGE = "El dragón {} lanza un rayo de fuego que causa {} de daño a {}."
OGRE_SMASH_MESSAGE = "El ogro {} golpea con fuerza y causa {} de daño a {}."
ASSASSIN_MESSAGE = "El asesino {} ataca con sigilo y causa {} de daño a {}."
UNDEAD_KNIGHT_MESSAGE = "El caballero no muerto {} ataca con su espada y causa {} de daño a {}."
WIZARD_MESSAGE = "El mago {} lanza un hechizo que causa {} de daño a {}."

def get_enemy_attack_message():
    return ENEMY_ATTACK_MESSAGE

def get_enemy_defeated_message():
    return ENEMY_DEFEATED_MESSAGE

def get_enemy_resurrected_message():
    return ENEMY_RESURRECTED_MESSAGE

def get_enemy_bleed_effect_message():
    return ENEMY_BLEED_EFFECT_MESSAGE

def get_enemy_evasion_message():
    return ENEMY_EVASION_MESSAGE

def get_enemy_angry_message():
    return ENEMY_ANGRY_MESSAGE

def get_enemy_magic_shield_message():
    return ENEMY_MAGIC_SHIELD_MESSAGE

def get_enemy_take_damage_message():
    return ENEMY_TAKE_DAMAGE_MESSAGE

def get_enemy_treasure_message():
    return ENEMY_TREASURE_MESSAGE

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

#mensajes de items
HEALING_ITEM_MESSAGE = "{} ha sido curado por {} puntos."
DAMAGE_BOOST_ITEM_MESSAGE = "El daño de {} ha aumentado en {} puntos."
SHIELD_ITEM_MESSAGE = "{} ha ganado {} puntos de escudo."

#mensajes de combates:
ENEMY_ENCOUNTER_MESSAGE = "Te encontraste con un enemigo."
COMBAT_MENU = "\n--- Menú de Combate ---\n1. Atacar\n2. Defenderse\n3. Huir"
INVALID_COMBAT_OPTION = "Opción de combate no válida. Inténtalo de nuevo."
PLAYER_ATTACK_MESSAGE = "{} atacó a {} causando {} puntos de daño."
ENEMY_ATTACK_MESSAGE = "{} atacó a {} causando {} puntos de daño."
PLAYER_DEFEND_MESSAGE = "{} se defiende."
ENEMY_DEFEND_MESSAGE = "{} se defiende."
PLAYER_FLEE_MESSAGE = "{} huye del combate."
ENEMY_FLEE_MESSAGE = "{} huye del combate."
PLAYER_DEFEAT_MESSAGE = "{} derrotó a {}."
ENEMY_DEFEAT_MESSAGE = "{} derrotó a {}." 
GAIN_EXPERIENCE_MESSAGE = "{} ganó {} puntos de experiencia."
LEVEL_UP_MESSAGE = "{} subió al nivel {}."

#mensajes de las dungeon
ENEMY_MESSAGE = "Te encontraste con un enemigo."
ATTACK_MESSAGE = "Has atacado a {} por {} puntos de daño."
DEFEND_MESSAGE = "Te has defendido."
FLEE_MESSAGE = "Has huido de la lucha."
ENEMY_DEFEATED_MESSAGE = "Has derrotado a {}!"
ITEM_FOUND_MESSAGE = "¡Has encontrado un objeto!"
HANDLE_ITEM_MESSAGE = "¿Qué deseas hacer con el objeto?"
PICK_UP_ITEM_MESSAGE = "Has agarrado el objeto."
DISCARD_ITEM_MESSAGE = "Has deshechado el objeto."
WRONG_DIRECTION = "No podes moverte en esa dirección porque está bloqueado el mapa."

def get_item_found_message():
    return ITEM_FOUND_MESSAGE

def get_handle_item_message():
    return HANDLE_ITEM_MESSAGE

def get_pick_up_item_message():
    return PICK_UP_ITEM_MESSAGE

def get_discard_item_message():
    return DISCARD_ITEM_MESSAGE


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

██████╗░██╗░░░██╗███╗░░██╗░██████╗░██████ █╗░█████╗░███╗░░██╗
██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗████╗░██║
██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║██╔██╗██║
██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║██║╚████║
██████╔╝╚██████╔╝ ██║░╚███║╚██████╔╝███████╗╚█████╔╝██║░╚███║
╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚══╝

Tu misión es derrotar al Dragón que amenaza con destruir el reino.
Para lograrlo, debes atravesar varias mazmorras llenas de enemigos peligrosos.
Buena suerte y... ¡Que comience la aventura!
"""

CHAPTER_1_NARRATIVE = """
Capítulo 1: La llamada a la Aventura
El jugador comienza su aventura en el pueblo de Cuadro Benegas,
donde se encuentra con un grupo de personajes que le piden ayuda
para derrotar al Dragón.
El jugador puede elegir entre tres héroes diferentes:
un guerrero, un mago y un arquero.
"""

CHAPTER_2_NARRATIVE = """
Capítulo 2: La Mazmorra del Dragón
El jugador se dirige a la mazmorra del Dragón,
donde se enfrenta a una serie de enemigos y obstáculos.
La mazmorra está llena de trampas y secretos,
y el jugador debe usar su habilidad y astucia para superarlos.
"""

CHAPTER_3_NARRATIVE = """
Capítulo 3: La Batalla Final
Finalmente, el jugador llega a la cámara del Dragón
y se enfrenta a él en una batalla épica.
El Dragón es un enemigo formidable,
pero el jugador puede usar todos los objetos y habilidades
que ha recogido durante su aventura para derrotarlo.
"""

