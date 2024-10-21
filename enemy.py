from characters import Character
from constant import (
    get_enemy_attack_message,
    get_enemy_defeated_message,
    get_enemy_resurrected_message,
    get_enemy_evasion_message,
    get_enemy_angry_message,    
    get_enemy_magic_shield_message,
    get_enemy_take_damage_message,
    get_enemy_treasure_message,
    get_assassin_message,
)

class Enemy(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

    def attack(self, player):
        damage = self.get_attack() - player.get_defense()
        damage = max(damage, 0) 
        player.take_damage(damage)
        print(get_enemy_attack_message().format(self.get_name(), player.get_name(), damage))

class AutomaticEnemy(Enemy): #! Ataque de enemigos 
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

    def act(self, player):
        self.attack(player)

class AncientDragon(AutomaticEnemy): #!Final boss
    def __init__(self):
        super().__init__("Ancient Dragon", 200, 75, 20)

    def special_ability(self, enemy):
        damage = self.get_strength() - self.get_defense()
        enemy.take_damage(damage)

    def take_damage(self, damage):
        reduced_damage = max(damage - self.get_defense(), 0)
        self.set_health(self.get_health() - reduced_damage)
        print(get_enemy_take_damage_message().format(self.get_name(), reduced_damage, self.get_health()))
        
        if self.get_health() <= 0:
            print(get_enemy_defeated_message().format(self.get_name()))

class Assassin(AutomaticEnemy):
    def __init__(self):
        super().__init__("Assassin", 100, 50, 20)
        self.evasion = False

    def special_ability(self, enemy):
        self.evasion = True
        print(get_enemy_evasion_message().format(self.get_name()))
        damage = self.get_attack() * 1.5
        enemy.take_damage(damage)
        print(get_assassin_message().format(self.get_name(), damage, enemy.get_name()))

    def take_damage(self, damage):
        if self.evasion:
            import random
            if random.random() < 0.5:
                print(get_enemy_evasion_message().format(self.get_name()))
                self.evasion = False
                return
        super().take_damage(damage)  # Usa el método take_damage de la clase base

class Ogre(AutomaticEnemy):
    def __init__(self):
        super().__init__("Ogre", 200, 32, 20)
        self.angry = False

    def special_ability(self):
        self.angry = True
        self.set_attack(self.get_attack() * 1.5)  # Cambié set_strength a set_attack
        print(get_enemy_angry_message().format(self.get_name(), self.get_attack()))

    def take_damage(self, damage):
        if self.angry:
            damage *= 0.8
        super().take_damage(damage)  # Usa el método take_damage de la clase base
        if self.get_health() <= 0:
            self.angry = False
            print(get_enemy_defeated_message().format(self.get_name()))
            self.award_treasure()

    def award_treasure(self):
        print(get_enemy_treasure_message())

class UndeadKnight(AutomaticEnemy):
    def __init__(self):
        super().__init__("Undead Knight", 120, 55, 25)
        self.resurrected = False

    def special_ability(self):
        self.resurrected = True
        self.set_health(self.get_health() + 50)
        print(get_enemy_resurrected_message().format(self.get_name(), self.get_health()))

    def take_damage(self, damage):
        if self.resurrected:
            damage *= 0.7
        super().take_damage(damage)  # Usa el método take_damage de la clase base
        if self.get_health() <= 0:
            self.resurrected = False
            print(get_enemy_defeated_message().format(self.get_name()))
            self.award_treasure()

    def award_treasure(self):
        print(get_enemy_treasure_message())

class Wizard(AutomaticEnemy):
    def __init__(self):
        super().__init__("Wizard", 80, 60, 10)
        self.magic_shield = False

    def special_ability(self):
        self.magic_shield = True
        self.set_defense(self.get_defense() + 10)
        print(get_enemy_magic_shield_message().format(self.get_name(), self.get_defense()))

    def take_damage(self, damage):
        if self.magic_shield:
            damage *= 0.9
        super().take_damage(damage)  # Usa el método take_damage de la clase base
        if self.get_health() <= 0:
            self.magic_shield = False
            print(get_enemy_defeated_message().format(self.get_name()))
            self.award_treasure()

    def award_treasure(self):
        print(get_enemy_treasure_message())