from constant import (
    WELCOME_MESSAGE,
    GAME_OVER_MESSAGE,
    LEVEL_UP_MESSAGE,
    FIGHT_MESSAGE,
    ATTACK_MESSAGE,
    DEFEND_MESSAGE,
    FLEE_MESSAGE,
    ENEMY_DEFEATED_MESSAGE,
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
        self.__current_level = 1

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
            print("No puedes moverte en esa dirección.")
            return

        self.__player.set_position((x, y))
        print(f"Te has movido a la posición {self.__player.get_position()}.")

        # Verifica si el jugador ha encontrado un enemigo o un objeto
        for enemy in self.__enemies:
            if enemy.get_position() == self.__player.get_position():
                self.__fight(enemy)
                break

        for item in self.__items:
            if item.get_position() == self.__player.get_position():
                self.__use_item(item)
                break

    def __fight(self, enemy):
        # Pelear contra el enemigo
        while enemy.get_health() > 0 and self.__player.get_health() > 0:
            print(FIGHT_MESSAGE)
            action = input("¿Qué deseas hacer? (atacar, defender, huir) ")
            if action == "atacar":
                enemy.set_health(enemy.get_health() - self.__player.get_strength())
                print(ATTACK_MESSAGE.format(enemy.get_name(), self.__player.get_strength()))
            elif action == "defender":
                self.__player.set_defense(self.__player.get_defense() + 10)
                print(DEFEND_MESSAGE)
            elif action == "huir":
                print(FLEE_MESSAGE)
                break

        if enemy.get_health() <= 0:
            print(ENEMY_DEFEATED_MESSAGE.format(enemy.get_name()))
            self.__player.set_experience(self.__player.get_experience() + 100)
            if self.__player.get_experience() >= 1000:
                self.__level_up()

    def __use_item(self, item):
        # Usar el objeto
        item.apply(self.__player)
        self.__items.remove(item)

    def __level_up(self):
        # Subir de nivel
        self.__player.set_level(self.__player.get_level() + 1)
        print(LEVEL_UP_MESSAGE)
        self.__current_level += 1
        self.__generate_level()

    def game_over(self):
        print(GAME_OVER_MESSAGE)

    # Métodos adicionales para el guardado y carga del juego se pueden agregar aquí
