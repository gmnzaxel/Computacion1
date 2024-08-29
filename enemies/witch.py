from characters import Character

class Brujo(Character):
    #! Habilidad especial del Brujo: Escudo Mágico y Drenaje de Fuerza
    def special_ability(self, enemy):
        # El escudo reduce el daño físico recibido a la mitad
        self.magic_shield = True
        print(f"{self.name} activó su Escudo Mágico, reduciendo el daño físico a la mitad.")

        # Drena parte de la fuerza del enemigo
        drained_strength = min(enemy.strength * 0.3, 5)  # Drena el 30% de la fuerza, con un máximo de 5 puntos
        enemy.strength -= drained_strength
        print(f"{self.name} drenó {drained_strength} puntos de fuerza de {enemy.name}.")

    #! Función para recibir daño con el escudo activo
    def take_damage(self, damage):
        if hasattr(self, 'magic_shield') and self.magic_shield:
            damage = damage * 0.5  # Reduce el daño a la mitad si el escudo está activo
        self.health -= damage
        print(f"{self.name} recibió {damage} puntos de daño.")
        self.magic_shield = False  # El escudo desaparece después de recibir daño