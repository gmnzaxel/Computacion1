from characters import Character

class Ogre(Character):
    def __init__(self, name, strength, defense, health):
        super().__init__(name, strength, defense, health)
        self.angry = False  # Indica si ya está enojado

    #! Habilidad especial del Ogre: Ira Desatada
    def special_ability(self):
        # El Ogre se enfurece y aumenta su fuerza
        self.angry = True
        self.strength *= 1.5  # Aumenta la fuerza en un 50%
        print(f"{self.name} está enojado y su fuerza ha aumentado a {self.strength}.")

    #! Función para recibir daño con un aumento de resistencia cuando está enojado
    def take_damage(self, damage):
        if self.angry:
            damage *= 0.8  # Reduce el daño recibido en un 20% cuando está enojado
        self.health -= damage
        print(f"{self.name} recibió {damage} puntos de daño y tiene {self.health} puntos de salud restantes.")
        if self.health <= 0:
            print(f"{self.name} ha sido derrotado.")
        # Después de recibir daño, el Ogre deja de estar enojado
        self.angry = False
