from characters import Character

class Assassin(Character):
    #! Habilidad especial del Asesino: Evasión y Golpe Letal
    def special_ability(self, enemy):
        # Aumenta la probabilidad de evadir ataques
        self.evasion = True
        print(f"{self.name} activó su Evasión, aumentando la posibilidad de esquivar ataques.")

        # Golpe letal que ignora la defensa del enemigo
        damage = self.strength * 1.5  # Golpe crítico que ignora la defensa
        enemy.take_damage(damage)
        print(f"{self.name} realizó un Golpe Letal y causó {damage} puntos de daño a {enemy.name}.")

    #! Función para recibir daño con una probabilidad de evasión
    def take_damage(self, damage):
        if hasattr(self, 'evasion') and self.evasion:
            import random
            if random.random() < 0.5:  # 50% de probabilidad de esquivar
                print(f"{self.name} evadió el ataque.")
                self.evasion = False  # La evasión se resetea después de usarla
                return
        self.health -= damage
        print(f"{self.name} recibió {damage} puntos de daño.")
        self.evasion = False
