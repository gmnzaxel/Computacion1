class Character:
    def __init__(self, name, health, strength, defense, level=1, experience=0):
        self.__name = name
        self.__health = health
        self.__strength = strength
        self.__defense = defense
        self.__level = level
        self.__experience = experience

   #! Funcion atacar
    def attack(self, enemy):
        damage = max(self.__strength - enemy.__defense, 0)
        enemy.__take_damage(damage)
        print(f"{self.__name} atacó a {enemy.__name} causando {damage} puntos de daño.")

    #! Funcion recibir daño, considerando defensa
    def take_damage(self, damage):
        actual_damage = max(damage - self.__defense, 0)
        self.__health -= actual_damage
        print(f"{self.__name}, recibiste {actual_damage} puntos de daño. Salud restante: {self.__health}")

    #! Funcion ganar experiencia
    def gain_experience(self, points):
        self.experience += points
        print(f"{self.name} ganó {points} puntos de experiencia.")
        self.check_level_up()

    #! Verificador de nivel
    def check_level_up(self):
        while self.experience >= self.level * 100:
            self.level_up()

    #! Funcion subir de nivel
    def level_up(self):
        self.level += 1
        self.health += 25  # Aumenta salud
        self.strength += 7  # Aumenta fuerza
        self.defense += 3   # Aumenta defensa
        self.experience -= self.level * 100
        print(f"{self.name} subió al nivel {self.level}!")
###################################
class Warrior:
    def _init_(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self, enemy):
        damage = max(self.strength - enemy.defense, 0)
        enemy.health -= damage
        print(f"{self.name} atacó a {enemy.name} causando {damage} puntos de daño.")

    def defend(self, enemy):
        reduced_damage = max(enemy.strength - self.defense * 2, 0)
        self.health -= reduced_damage
        print(f"{self.name} se defiende. Recibió {reduced_damage} puntos de daño reducido.")
