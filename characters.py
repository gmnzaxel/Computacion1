from constant import (
    get_attack_message,
    get_take_damage_message,
    get_level_up_message, 
    get_gain_experience_message
)

class Character:

    def __init__(self, name, health, strength, defense, level=1, experience=0, critical_chance=0, special_ability=None):
        self.__name = name
        self.__health = health
        self.__strength = strength
        self.__defense = defense
        self.__level = level
        self.__experience = experience
        self.__critical_chance = critical_chance
        self.__special_ability = special_ability
        self.__position = (0, 0)

    # Getters y setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_strength(self):
        return self.__strength

    def set_strength(self, strength):
        self.__strength = strength

    def get_defense(self):
        return self.__defense

    def set_defense(self, defense):
        self.__defense = defense

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience

    def get_critical_chance(self):
        return self.__critical_chance

    def set_critical_chance(self, critical_chance):
        self.__critical_chance = critical_chance

    def get_special_ability(self):
        return self.__special_ability

    def set_special_ability(self, special_ability):
        self.__special_ability = special_ability

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position

    #! Función atacar
    def attack(self, enemy):
        damage = max(self.get_strength() - enemy.get_defense(), 0)
        enemy.take_damage(damage)
        print(get_attack_message().format(self.get_name(), enemy.get_name(), damage))

    #! Función recibir daño, considerando defensa
    def take_damage(self, damage):
        actual_damage = max(damage - self.get_defense(), 0)
        self.set_health(self.get_health() - actual_damage)
        print(get_take_damage_message().format(self.get_name(), actual_damage, self.get_health()))

    #! Función ganar experiencia
    def gain_experience(self, points):
        self.set_experience(self.get_experience() + points)
        print(get_gain_experience_message().format(self.get_name(), points))
        self.check_level_up()

    #! Verificador de nivel
    def check_level_up(self):
        while self.get_experience() >= self.get_level() * 100:
            self.level_up()

    #! Función subir de nivel
    def level_up(self):
        self.set_level(self.get_level() + 1)
        self.set_health(self.get_health() + 25)  # Aumenta salud
        self.set_strength(self.get_strength() + 7)  # Aumenta fuerza
        self.set_defense(self.get_defense() + 3)   # Aumenta defensa
        self.set_experience(self.get_experience() - self.get_level() * 100)
        print(get_level_up_message().format(self.get_name(), self.get_level()))