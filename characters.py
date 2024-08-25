class Character:
    def __init__(self, name, health, strength, defense, level=1, experience=0):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.level = level
        self.experience = experience

   #! Funcion atacar
    def attack(self, enemy):
        damage = max(self.strength - enemy.defense, 0)
        enemy.take_damage(damage)
        print(f"{self.name} atacó a {enemy.name} causando {damage} puntos de daño.")

    #! Funcion recibir daño, considerando defensa
    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health -= actual_damage
        print(f"{self.name}, recibiste {actual_damage} puntos de daño. Salud restante: {self.health}")

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

class Warrior(Character):
    #! Habilidad especial del luchador: ataque con aumento de daño
    def special_ability(self, enemy):
        damage = max(self.strength * 2.5 - enemy.defense, 0)
       # TODO enemy.FUNCION TOMAR DAÑO DE LOS ENEMIGOS(damage)
        print(f"{self.name} usó su habilidad especial y causó {damage} puntos de daño a {enemy.name}.")

class Mage(Character):
    #! Habilidad especial del mago: hechizo que ignora parte de la defensa del enemigo
    def cast_spell(self, enemy):
        damage = max(self.strength * 1.8 - enemy.defense * 0.5, 0)
       # TODO enemy.take_damage(damage)
        print(f"{self.name} lanzó un hechizo crítico y causó {damage} puntos de daño a {enemy.name}.")

class Archer(Character):
    #! Habilidad especial del arquero: ataque a distancia con posibilidad de golpe crítico
    def shoot_arrow(self, enemy):
        critical_hit = 1.5 if self.level % 2 == 0 else 1  # Golpe crítico en niveles pares
        damage = max(self.strength * 1.3 * critical_hit - enemy.defense, 0)
        # TODO enemy.take_damage(damage)
        if critical_hit > 1:
            print(f"¡{self.name} realizó un golpe crítico!")
        print(f"{self.name} disparó una flecha causando {damage} puntos de daño a {enemy.name}.")
