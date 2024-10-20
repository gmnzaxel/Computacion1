from constant import (
    WELCOME_MESSAGE,
    GAME_OVER_MESSAGE,
    LEVEL_UP_MESSAGE,
    COMBAT_MENU,
    INVALID_COMBAT_OPTION,
    PLAYER_ATTACK_MESSAGE,
    ENEMY_ATTACK_MESSAGE,
    PLAYER_DEFEND_MESSAGE,
    PLAYER_FLEE_MESSAGE,
    PLAYER_DEFEAT_MESSAGE,
    ENEMY_DEFEAT_MESSAGE,
    GAIN_EXPERIENCE_MESSAGE,
    LEVEL_UP_MESSAGE,
    get_item_found_message,
    get_handle_item_message,
    get_pick_up_item_message,
    get_discard_item_message,
    WRONG_DIRECTION,
    ENEMY_MESSAGE,
    INVALID_OPTION,
    HEALTH_GAIN_MESSAGE,
    CURRENT_HEALTH_MESSAGE,
    OBJECT_MENU,
    CHECK_BOSS,
    COMBAT_MENU_DRAGON,
    ASK_ACTIONS,
    FOUND_DRAGON,
    WIN_GAME_OVER,
    CANT_SCAPE,
    PLAYER_MOVE_MESSAGE,
    
)
from item import (
    HealingItem,
    DamageBoostItem,
    ShieldItem,
)
from characters import Character
import random

from enemy import *

class Dungeon:
    def __init__(self, width, height, player):
        self.__width = width
        self.__height = height
        self.__player = player
        self.__enemies = []
        self.__items = []
        self.__collected_items = set()
        self.__defeated_enemies = set()
        self._current_level = 1
        self._enemy_found = False
        self.__visited_positions = set()

    def get_enemy_found(self):
        return self._enemy_found

    def set_enemy_found(self, found):
        self._enemy_found = found

    def start_game(self):
        print(WELCOME_MESSAGE)
        self.generate_level()

    def generate_level(self):
        # Genera un nivel con enemigos y objetos
        for _ in range(5):
            enemy = random.choice([Assassin(), Ogre(), UndeadKnight(), Wizard()])
            enemy.set_position((random.randint(0, self.__width - 1), random.randint(0, self.__height - 1)))
            self.__enemies.append(enemy)

        for _ in range(3):
            item_type = random.choice([HealingItem, DamageBoostItem, ShieldItem])
            item = item_type("Objeto", 10)
            item.set_position((random.randint(0, self.__width - 1), random.randint(0, self.__height - 1)))
            self.__items.append(item)


    def check_for_boss(self):
        #todo if len(self.__collected_items) == len(self.__items) and len(self.__defeated_enemies) == len(self.__enemies):
        #todo     print(CHECK_BOSS)
        
        #! Si todos los enemigos han sido derrotados, se genera el jefe final
        if len(self.__defeated_enemies) == len(self.__enemies):
            print(CHECK_BOSS)
            # Generar el jefe final
            ancient_dragon = AncientDragon()
            ancient_dragon.set_position((random.randint(0, self._width - 1), random.randint(0, self._height - 1)))
            self.__enemies.append(ancient_dragon)
            print(CHECK_BOSS)
 
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
            self.__print_map()
            return

        self.__player.set_position((x, y))
        print(PLAYER_MOVE_MESSAGE.format(self.__player.get_position()))
        self.__visited_positions.add((x, y))
        self.__print_map()

        # Verifica si el jugador ha encontrado un enemigo o un objeto
        for enemy in self.__enemies:
            if enemy.get_position() == self.__player.get_position():
                print(ENEMY_MESSAGE)
                self.combat(enemy)
                self.__enemies.remove(enemy)
                if len(self.__enemies) == 0:
                    ancient_dragon = AncientDragon()
                    ancient_dragon.set_position((random.randint(0, self.__width - 1), random.randint(0, self.__height - 1)))
                    self.__enemies.append(ancient_dragon)
                break

        for item in self.__items:
            if item.get_position() == self.__player.get_position():
                print(get_item_found_message())
                self.__handle_item(item)
                break

    def attempt_flee(self):
        if random.randint(1, 10) <= 3:  # 30% de probabilidad de escape
                print(PLAYER_FLEE_MESSAGE.format(self.__player.get_name()))
                return True
        else:
                self.__player.set_health(self.__player.get_health() - random.randint(10, 20))
                print(CANT_SCAPE)
                print(CURRENT_HEALTH_MESSAGE.format(self.__player.get_name(), self.__player.get_health()))
                return False

    def combat(self, enemy):
        if isinstance(enemy, AncientDragon):
            print(FOUND_DRAGON)
            # combate para AncientDragon
            while enemy.get_health() > 0 and self.__player.get_health() > 0:
                print(COMBAT_MENU_DRAGON)
                action = input(ASK_ACTIONS)

                # Bucle para manejar opciones inválidas
                while action not in ["1", "2"]:
                    print(INVALID_COMBAT_OPTION)
                    action = input(ASK_ACTIONS)

                if action == "1":
                    # Atacar al AncientDragon
                    damage = self.__player.get_strength() - enemy.get_defense()
                    if damage > 0:
                        enemy.set_health(enemy.get_health() - damage)
                        print(PLAYER_ATTACK_MESSAGE.format(self.__player.get_name(), enemy.get_name(), damage))
                    else:
                        print(PLAYER_DEFEND_MESSAGE.format(self.__player.get_name()))
                elif action == "2":
                    # Defenderse del AncientDragon
                    self.__player.set_defense(self.__player.get_defense() + 10)
                    print(PLAYER_DEFEND_MESSAGE.format(self.__player.get_name()))

                # Turno del AncientDragon
                if enemy.get_health() > 0:
                    enemy.special_ability(self.__player)

                # Verificar si jugador ha sido atacado
                if self.__player.get_health() <= 0:
                    print(ENEMY_DEFEAT_MESSAGE.format(enemy.get_name(), self.__player.get_name()))
                    return False  # Indica que el juego ha terminado

            # Verificar quién ganó el combate
            if enemy.get_health() <= 0:
                print(PLAYER_DEFEAT_MESSAGE.format(self.__player.get_name(), enemy.get_name()))
                self.__player.set_experience(self.__player.get_experience() + 1000)
                print(GAIN_EXPERIENCE_MESSAGE.format(self.__player.get_name(), 1000))
                print(WIN_GAME_OVER)
                exit()
        else:
            # Lógica de combate normal para otros enemigos
            while enemy.get_health() > 0 and self.__player.get_health() > 0:
                print(COMBAT_MENU)
                action = input(ASK_ACTIONS)

                # Bucle para manejar opciones inválidas
                while action not in ["1", "2", "3"]:  # Asegúrate de que la opción sea válida
                    print(INVALID_COMBAT_OPTION)
                    action = input(ASK_ACTIONS)  # Vuelve a pedir la acción

                if action == "1":
                    # Atacar al enemigo
                    damage = max(0, self.__player.get_strength() * 1.5 - enemy.get_defense() + random.randint(-5, 5))
                    enemy.set_health(enemy.get_health() - damage)
                    print(PLAYER_ATTACK_MESSAGE.format(self.__player.get_name(), enemy.get_name(), damage))

                    # Verificar si el enemigo ha sido derrotado
                    if enemy.get_health() <= 0:
                        print(PLAYER_DEFEAT_MESSAGE.format(self.__player.get_name(), enemy.get_name()))
                        self.__player.set_experience(self.__player.get_experience() + 100)
                        print(GAIN_EXPERIENCE_MESSAGE.format(self.__player.get_name(), 100))
                        if self.__player.get_experience() >= 1000:
                            self.__level_up()
                        return True  # Indica que el combate ha terminado

                elif action == "2":
                    # Defenderse del enemigo
                    self.__player.set_defense(self.__player.get_defense() + 10)
                    print(PLAYER_DEFEND_MESSAGE.format(self.__player.get_name()))
                elif action == "3":
                    # Huir del combate
                    if self.attempt_flee():
                        break  # Salir del combate

                    # Turno del enemigo
                    if enemy.get_health() > 0 and action != "3":
                        damage = max(0, enemy.get_strength() - self.__player.get_defense() + random.randint(-5, 5))
                        self.__player.set_health(self.__player.get_health() - damage)
                        print(ENEMY_ATTACK_MESSAGE.format(enemy.get_name(), self.__player.get_name(), damage))
                        print(CURRENT_HEALTH_MESSAGE.format(self.__player.get_name(), self.__player.get_health()))
                        print(CURRENT_HEALTH_MESSAGE.format(enemy.get_name(), enemy.get_health()))

                    # Verificar si el jugador ha sido derrotado
                    if self.__player.get_health() <= 0:
                        print(ENEMY_DEFEAT_MESSAGE.format(enemy.get_name(), self.__player.get_name()))
                        print(GAME_OVER_MESSAGE)
                        exit()
                        return False  # juego terminado

                    # Verificar quién gano el combate
                    if enemy.get_health() <= 0:
                        print(PLAYER_DEFEAT_MESSAGE.format(self.__player.get_name(), enemy.get_name()))
                        self.__player.set_experience(self.__player.get_experience() + 100)
                        print(GAIN_EXPERIENCE_MESSAGE.format(self.__player.get_name(), 100))
                        self.__player.set_health(self.__player.get_health() + 20)
                        print(HEALTH_GAIN_MESSAGE.format(self.__player.get_name(), 20))
                        print(CURRENT_HEALTH_MESSAGE.format(self.__player.get_name(), self.__player.get_health()))
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
                # elif (x, y) in [enemy.get_position() for enemy in self.__enemies]:
                #     divisor += " E |"
                # elif ( x, y) in [item.get_position() for item in self.__items]:
                #     divisor += " O |"
                else:
                    divisor += "   |"
            print(divisor)
            print("  +" + "---+" * self.__width)

    def __handle_item(self, item):
        while True:
            print(OBJECT_MENU)
            action = input(get_handle_item_message())
            
            if action == "1":
                # Agarrar el objeto
                item.apply(self.__player)
                print(get_pick_up_item_message())
                self.__items.remove(item)
                break
            elif action == "2":
                # Dejar el objeto
                print(get_discard_item_message())
                break
            else:
                print(INVALID_OPTION)
    

        self.check_for_boss()    
    
    def __level_up(self):
        self.__player.set_level(self.__player.get_level() + 1)
        self.__player.set_health(self.__player.get_health() + 25)
        self.__player.set_strength(self.__player.get_strength() + 7)
        self.__player.set_defense(self.__player.get_defense() + 3)
        print(LEVEL_UP_MESSAGE.format(self.__player.get_name(), self.__player.get_level()))