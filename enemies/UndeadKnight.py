from characters import Character

class UndeadKnight(Character):
    def __init__(self, name, strength, defense, health):
        super().__init__(name, strength, defense, health)
        self.resurrected = False  # Indica si ya ha sido resucitado

    #! Habilidad especial del Caballero No Muerto: Golpe Maldito
    def special_ability(self, enemy):
        # Golpe Maldito que inflige daño adicional basado en la salud máxima del enemigo
        damage = self.strength * 2 + enemy.health * 0.2
        enemy.take_damage(damage)
        print(f"{self.name} usó su Golpe Maldito y causó {damage} puntos de daño a {enemy.name}.")

    #! Función para recibir daño con posibilidad de resucitar
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0 and not self.resurrected:
            self.resurrect()
        elif self.health > 0:
            print(f"{self.name} recibió {damage} puntos de daño y le quedan {self.health} puntos de salud.")
        else:
            print(f"{self.name} ha sido derrotado.")

    #! Función de resurrección
    def resurrect(self):
        self.resurrected = True
        self.health = max(self.health * 0.5, 50)  # Resucita con el 50% de la salud o un mínimo de 50 puntos
        print(f"{self.name} ha resucitado con {self.health} puntos de salud.")

        #ogre
        class Ogre(Character):
            def __init__(self, name, strength, defense, health):
                super().__init__(name, strength, defense, health)
                self.angry = False  # Indica si ya está enojado
                
