class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    # def apply(self, target):
    #     """Aplica el efecto del ítem en el objetivo."""
    #     raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def __str__(self):
        return f"{self.name} - Efecto: {self.effect}"

#TODO Cada clase va en una carpeta pero ni ganas de hacerlas ahora
#Curación por si no sabes q es healing botardo
class HealingItem(Item):
    def __init__(self, name, healing_amount):
        super().__init__(name, f"Cura {healing_amount} puntos de vida")
        self.healing_amount = healing_amount

    def apply(self, target):
        if target.health > 0:
            target.health += self.healing_amount
            print(f"{target.name} ha sido curado por {self.healing_amount} puntos de vida.")
        else:
            print(f"{target.name} no puede ser curado porque está muerto.")

#mas daño papaa
class DamageBoostItem(Item):
    def __init__(self, name, damage_increase):
        super().__init__(name, f"Aumenta el daño en {damage_increase} puntos")
        self.damage_increase = damage_increase

    def apply(self, target):
        target.damage += self.damage_increase
        print(f"El daño de {target.name} ha aumentado en {self.damage_increase} puntos.")

#escuditoo
class ShieldItem(Item):
    def __init__(self, name, shield_amount):
        super().__init__(name, f"Añade {shield_amount} puntos de escudo")
        self.shield_amount = shield_amount

    def apply(self, target):
        target.shield += self.shield_amount
        print(f"{target.name} ha ganado {self.shield_amount} puntos de escudo.")
##instaa kill 
# class DeathItem(Item):
#     def __init__(self, name):
#         super().__init__(name, "Causa muerte instantánea")

#     def apply(self, target):
#         target.health = 0
#         print(f"{target.name} ha sido eliminado instantáneamente.")

#TODO instaa kill pero al enemigo


#! EJEMPLO DE USO SEGUN GPT
# Creando enemigos
# goblin = Enemy(name="Goblin", health=100, shield=50, damage=15)

# # Creando ítems
# potion = HealingItem(name="Poción de Vida", healing_amount=30)
# damage_boost = DamageBoostItem(name="Espada de Fuego", damage_increase=10)
# shield_boost = ShieldItem(name="Escudo Mágico", shield_amount=25)
# death_scroll = DeathItem(name="Pergamino de Muerte")

# # Usando ítems en el enemigo
# print(goblin)
# potion.apply(goblin)
# damage_boost.apply(goblin)
# shield_boost.apply(goblin)
# death_scroll.apply(goblin)
# print(goblin)
