from characters import Character

class AncientDragon(Character):
    def __init__(self, name, strength, defense, health):
        super().__init__(name, strength, defense, health)
        self.defeated = False  # Indica si el dragón ha sido derrotado

    #! Habilidad especial del AncientDragon: Tormenta de Escamas
    def special_ability(self, enemy):
        # Tormenta de Escamas que inflige daño y tiene una probabilidad de causar un efecto de sangrado
        import random
        damage = self.strength * 2
        bleed_chance = 0.3  # 30% de probabilidad de causar sangrado
        enemy.take_damage(damage)
        print(f"{self.name} usa su Tormenta de Escamas y causa {damage} puntos de daño a {enemy.name}.")
        
        if random.random() < bleed_chance:
            enemy.apply_bleed_effect()
            print(f"{enemy.name} está sangrando y recibirá daño adicional en los próximos turnos.")

    #! Función para recibir daño con alta resistencia
    #!Revisar si no es muy complicado
    def take_damage(self, damage):
        # Reduce el daño recibido por su alta defensa
        reduced_damage = max(damage - self.defense, 0)
        self.health -= reduced_damage
        print(f"{self.name} recibe {reduced_damage} puntos de daño y tiene {self.health} puntos de salud restantes.")
        
        if self.health <= 0:
            self.defeated = True
            print(f"{self.name} ha sido derrotado. ¡Has ganado una recompensa especial!")

            # Llama a la función de recompensa al derrotarlo
            self.award_treasure()

    #! Función para otorgar una recompensa al jugador
    def award_treasure(self):
        # Aquí, el jugador recibe una recompensa en lugar de un aumento de estadísticas
        print("¡Has derrotado al Ancient Dragon y obtienes una recompensa especial!")
        print("¡Encuentras un cofre con un objeto raro dentro!")

    #! Función para aplicar el efecto de sangrado
    def apply_bleed_effect(self):
        # Este es un ejemplo de cómo podrías aplicar un efecto de sangrado
        print(f"{self.name} está sangrando, recibiendo daño adicional en los próximos turnos.")
