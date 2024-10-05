from characters import Character
from constant import (get_attack_message)

class Hero(Character):
    def __init__(self, name, health, strength, defense, level=1, experience=0):
        super().__init__(name, health, strength, defense, level, experience)

class Archer(Hero):
    def shoot_arrow(self, enemy):
        critical_hit = 1.5 if self.get_level() % 2 == 0 else 1  # Golpe crítico en niveles pares
        damage = max(self.get_strength() * 1.3 * critical_hit - enemy.get_defense(), 0)
        enemy.take_damage(damage)
        print(get_attack_message().format(self.get_name(), enemy.get_name(), damage))

class Mage(Hero):
    def cast_spell(self, enemy):
        damage = max(self.get_strength() * 1.8 - enemy.get_defense() * 0.5, 0)
        enemy.take_damage(damage)
        print(get_attack_message().format(self.get_name(), enemy.get_name(), damage))

class Warrior(Hero):
    def special_ability(self, enemy):
        damage = max(self.get_strength() * 2.5 - enemy.get_defense(), 0)
        enemy.take_damage(damage)
        print(get_attack_message().format(self.get_name(), enemy.get_name(), damage))
