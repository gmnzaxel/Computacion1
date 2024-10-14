from constant import (
    WELCOME_MESSAGE,
    GAME_OVER_MESSAGE,
    LEVEL_UP_MESSAGE,
    ENEMY_ENCOUNTER_MESSAGE,
    COMBAT_MENU,
    INVALID_COMBAT_OPTION,
    PLAYER_ATTACK_MESSAGE,
    ENEMY_ATTACK_MESSAGE,
    PLAYER_DEFEND_MESSAGE,
    ENEMY_DEFEND_MESSAGE,
    PLAYER_FLEE_MESSAGE,
    ENEMY_FLEE_MESSAGE,
    PLAYER_DEFEAT_MESSAGE,
    ENEMY_DEFEAT_MESSAGE,
    GAIN_EXPERIENCE_MESSAGE,
    LEVEL_UP_MESSAGE,
    ENEMY_DEFEATED_MESSAGE,
    get_item_found_message,
    get_handle_item_message,
    get_pick_up_item_message,
    get_discard_item_message,
    WRONG_DIRECTION,
    ENEMY_MESSAGE,
    
)
from item import (
    HealingItem,
    DamageBoostItem,
    ShieldItem,
)
from characters import Character
import random

class Dungeon:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__player = Character("Jugador", 100, 10, 5)
        self.__enemies = []
        self.__items = []
        self._current_level = 1
        self._enemy_found = False
        self.__visited_positions = set()

    def get_enemy_found(self):
        return self._enemy_found

    def set_enemy_found(self, found):
        self._enemy_found = found

    def start_game(self):
        print(WELCOME_MESSAGE)
        self.__generate_level()

    def __generate_level(self):
        # Genera un nivel con enemigos y objetos
        for _ in range(5):
            enemy = Character("Enemigo", 10, 2, 1)  # Sin probabilidad, ya que no se utilizó
            enemy.set_position((random.randint(0, self.__width - 1), random.randint(0, self.__height - 1)))
            self.__enemies.append(enemy)

        for _ in range(3):
            item_type = random.choice([HealingItem, DamageBoostItem, ShieldItem])
            item = item_type("Objeto", 10)
            item.set_position((random.randint(0, self.__width - 1), random.randint(0, self.__height - 1)))
            self.__items.append(item)

    def navigate(self, direction):
        # Mueve al jugador en la dirección especificada
        x, y = self.__player.get_position()
        if direction == "norte" and y > 0:
            y -= 1
        elif direction == "sur" and y < self.__height - 1:
            y += 1
        elif direction == "este" and x < self.__width - 1:
            x += 1
        elif direction == "oeste" and x > 0:
            x -= 1
        else:
            print(WRONG_DIRECTION)
            return


        self.__player.set_position((x, y))
        print(f"Te moviste a la posición {self.__player.get_position()}.")
        self.__visited_positions.add((x, y))
        self.__print_map()

        # Verifica si el jugador ha encontrado un enemigo o un objeto
        for enemy in self.__enemies:
            if enemy.get_position() == self.__player.get_position():
                print(ENEMY_MESSAGE)
                self.__combat(enemy)
                break

        for item in self.__items:
            if item.get_position() == self.__player.get_position():
                print(get_item_found_message())
                self.__handle_item(item)
                break

    def __combat(self, enemy):
        while enemy.get_health() > 0 and self.__player.get_health() > 0:
            print(COMBAT_MENU)
            action = input("¿Qué deseas hacer? ")
            if action == "1":
                # Atacar al enemigo
                damage = self.__player.get_strength() - enemy.get_defense()
                if damage > 0:
                    enemy.set_health(enemy.get_health() - damage)
                    print(PLAYER_ATTACK_MESSAGE.format(self.__player.get_name(), enemy.get_name(), damage))
                else:
                    print(PLAYER_DEFEND_MESSAGE.format(self.__player.get_name()))
            elif action == "2":
                # Defenderse del enemigo
                self.__player.set_defense(self.__player.get_defense() + 10)
                print(PLAYER_DEFEND_MESSAGE.format(self.__player.get_name()))
            elif action == "3":
                # Huir del combate
                print(PLAYER_FLEE_MESSAGE.format(self.__player.get_name()))
                break
            else:
                print(INVALID_COMBAT_OPTION)

            # Turno del enemigo
            if enemy.get_health() > 0:
                damage = enemy.get_strength() - self.__player.get_defense()
                if damage > 0:
                    self.__player.set_health(self.__player.get_health() - damage)
                    print(ENEMY_ATTACK_MESSAGE.format(enemy.get_name(), self.__player.get_name(), damage))
                else:
                    print(ENEMY_DEFEND_MESSAGE.format(enemy.get_name()))

        # Verificar quién ganó el combate
        if enemy.get_health() <= 0:
            print(PLAYER_DEFEAT_MESSAGE.format(self.__player.get_name(), enemy.get_name()))
            self.__player.set_experience(self.__player.get_experience() + 100)
            print(GAIN_EXPERIENCE_MESSAGE.format(self.__player.get_name(), 100))
            if self.__player.get_experience() >= 1000:
                self.__level_up()
        elif self.__player.get_health() <= 0:
            print(ENEMY_DEFEAT_MESSAGE.format(enemy.get_name(), self.__player.get_name()))

    # mapa del juego
    def __print_map(self): # mapa
        print("  +" + "---+" * self.__width)
        for y in range(self.__height):
            divisor = "|"
            for x in range(self.__width):
                if (x, y) == self.__player.get_position():
                    divisor += " P |"
                elif (x, y) in self.__visited_positions:
                    divisor += " / |"
                elif (x, y) in [enemy.get_position() for enemy in self.__enemies]:
                    divisor += " E |"
                elif (x, y) in [item.get_position() for item in self.__items]:
                    divisor += " I |"
                else:
                    divisor += " * |"
            print(divisor)
            print("  +" + "---+" * self.__width)

    def __level_up(self):
        self.__player.set_level(self.__player.get_level() + 1)
        print(LEVEL_UP_MESSAGE.format(self.__player.get_name(), self.__player.get_level()))
        # Aumentar atributos del personaje al subir de nivel
        self.__player.set_health(self.__player.get_health() + 5)
        self.__player.set_strength(self.__player.get_strength() + 3)
        self.__player.set_defense(self.__player.get_defense() + 2)


    def __handle_item(self, item):
        # Manipular objeto
        print(get_handle_item_message())
        action = input("(agarrar, deshechar) ")
        if action == "agarrar":
            item.apply(self.__player)
            self.__items.remove(item)
            print(get_pick_up_item_message())
        elif action == "deshechar":
            print(get_discard_item_message())
            self.__items.remove(item)

    def game_over(self):
        print(GAME_OVER_MESSAGE)
