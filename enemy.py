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
    get_dragon_fire_message,
    get_assassin_message,
)

class Enemy(Character):
    def __init__(self, name, health, attack, defense, level=1, experience=0, critical_chance=0, special_ability=None):
        super().__init__(name, health, attack, defense, level, experience, critical_chance, special_ability)

    def attack(self, player):
        damage = max(self.get_strength() - player.get_defense(), 0)
        player.take_damage(damage)
        print(get_enemy_attack_message().format(self.get_name(), player.get_name(), damage))

class AutomaticEnemy(Enemy):
    # enemigo actúa automáticamente
    def act(self, player):
        self.attack(player)

class AncientDragon(AutomaticEnemy):
    def __init__(self):
        super().__init__("Ancient Dragon", 200, 40, 20)
        self.defeated = False

    # habilidad especial dragon 
    def special_ability(self, enemy):
        import random
        damage = self.get_strength() * random.uniform(1.0, 2.0) # uniform: num flotante
        enemy.take_damage(damage)
        print(get_dragon_fire_message().format(self.get_name, damage, enemy.get_name()))
        

    # dragón antiguo recibe daño
    def take_damage(self, damage):
        reduced_damage = max(damage - self.get_defense(), 0)
        self.set_health(self.get_health() - reduced_damage)
        print(get_enemy_take_damage_message().format(self.get_name(), reduced_damage, self.get_health()))
        
        if self.get_health() <= 0:
            self.defeated = True
            print(get_enemy_defeated_message().format(self.get_name()))
            self.award_treasure()

    # dragón antiguo tesoro
    def award_treasure(self):
        print(get_enemy_treasure_message())

class Assassin(AutomaticEnemy):
    def __init__(self):
        super().__init__("Assassin", 100, 25, 15)

    # asesino habilidad especial
    def special_ability(self, enemy):
        self.evasion = True
        print(get_enemy_evasion_message().format(self.get_name()))
        damage = self.get_strength() * 1.5
        enemy.take_damage(damage)
        print(get_assassin_message().format(self.get_name(), damage, enemy.get_name()))

    def take_damage(self, damage):
        if hasattr(self, 'evasion') and self.evasion:
            import random
            if random.random() < 0.5:
                print(get_enemy_evasion_message().format(self.get_name()))
                self.evasion = False
                return
        self.set_health(self.get_health() - damage)
        print(get_enemy_take_damage_message().format(self.get_name(), damage, self.get_health()))
        self.evasion = False

class Ogre(AutomaticEnemy):
    def __init__(self):
        super().__init__("Ogre", 200, 15, 20)
        self.angry = False

    # ogro habilidad especial
    def special_ability(self):
        self.angry = True
        self.set_strength(self.get_strength() * 1.5)
        print(get_enemy_angry_message().format(self.get_name(), self.get_strength()))

    def take_damage(self, damage):
        if self.angry:
            damage *= 0.8
        self.set_health(self.get_health() - damage)
        print(get_enemy_take_damage_message().format(self.get_name(), damage, self.get_health()))
        if self.get_health() <= 0:
            self.angry = False
            print(get_enemy_defeated_message().format(self.get_name()))
            self.award_treasure()

    # tesoro
    def award_treasure(self):
        print(get_enemy_treasure_message())

class UndeadKnight(AutomaticEnemy):
    def __init__(self):
        super().__init__("Undead Knight", 150, 20, 25)
        self.resurrected = False

    # caballero habilidad especial
    def special_ability(self):
        self.resurrected = True
        self.set_health(self.get_health() + 50)
        print(get_enemy_resurrected_message().format(self.get_name(), self.get_health()))

    # recibe daño
    def take_damage(self, damage):
        if self.resurrected:
            damage *= 0.7
        self.set_health(self.get_health() - damage)
        print(get_enemy_take_damage_message().format(self.get_name(), damage, self.get_health()))
        if self.get_health() <= 0:
            self.resurrected = False
            print(get_enemy_defeated_message().format(self.get_name()))
            self.award_treasure()

    # tesoro
    def award_treasure(self):
        print(get_enemy_treasure_message())

class Wizard(AutomaticEnemy):
    def __init__(self):
        super().__init__("Wizard", 80, 30, 15)
        self.magic_shield = False

    # mago habilidad especial
    def special_ability(self):
        self.magic_shield = True
        self.set_defense(self.get_defense() + 10)
        print(get_enemy_magic_shield_message().format(self.get_name(), self.get_defense()))

    def take_damage(self, damage):
        if self.magic_shield:
            damage *= 0.9
        self.set_health(self.get_health() - damage)
        print(get_enemy_take_damage_message().format(self.get_name(), damage, self.get_health()))
        if self.get_health() <= 0:
            self.magic_shield = False
            print(get_enemy_defeated_message().format(self.get_name()))
            self.award_treasure()

    # tesoro
    def award_treasure(self):
        print(get_enemy_treasure_message())