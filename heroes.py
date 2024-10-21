from characters import Character
from constant import (
    get_attack_message,
    PLAYER_TAKE_DAMAGE_MESSAGE,
    PLAYER_DEFEATED_MESSAGE,
    
    )

class Player(Character):
    def take_damage(self, damage):
        self.set_health(self.get_health() - damage)
        print(PLAYER_TAKE_DAMAGE_MESSAGE.format(self.get_name(), damage, self.get_health()))
        if self.get_health() <= 0:
            print(PLAYER_DEFEATED_MESSAGE.format(self.get_name()))

class Hero(Character):
    def __init__(self, name, health, strength, defense, level=1, experience=0):             
        super().__init__(name, health, strength, defense, level, experience)

class Archer(Hero):
    def shoot_arrow(self, enemy):
        critical_hit = 1.5 if self.get_level() % 2 == 0 else 1  #! Golpe crítico en niveles pares
        damage = self.get_strength() * 1.3 * critical_hit - enemy.get_defense()
        enemy.take_damage(damage)
        print(get_attack_message().format(self.get_name(), enemy.get_name(), damage))

class Mage(Hero):
    def cast_spell(self, enemy):
        damage = self.get_strength() * 1.8 - enemy.get_defense() * 0.5
        enemy.take_damage(damage)
        print(get_attack_message().format(self.get_name(), enemy.get_name(), damage))

class Warrior(Hero):
    def special_ability(self, enemy):
        damage = self.get_strength() * 2.5 - enemy.get_defense()
        enemy.take_damage(damage)
        print(get_attack_message().format(self.get_name(), enemy.get_name(), damage))