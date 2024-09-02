class Item:
    def __init__(self, name, effect):
        self.__name = name
        self.__effect = effect

    # def apply(self, target):
    #     """Aplica el efecto del ítem en el objetivo."""
    #     raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def __str__(self):
        return f"{self.__name} - Efecto: {self.__effect}"

class HealingItem(Item):
    def __init__(self, name, healing_amount):
        super().__init__(name, f"Cura {healing_amount} puntos de vida")
        self.__healing_amount = healing_amount

    def apply(self, target):
        if target.__health > 0:
            target.__health += self.__healing_amount
            print(f"{target.__name} ha sido curado por {self.__healing_amount} puntos de vida.")
        else:
            print(f"{target.__name} no puede ser curado porque está muerto.")

#mas daño papaa
class DamageBoostItem(Item):
    def __init__(self, name, damage_increase):
        super().__init__(name, f"Aumenta el daño en {damage_increase} puntos")
        self.__damage_increase = damage_increase

    def apply(self, target):
        target.__damage += self.__damage_increase
        print(f"El daño de {target.__name} ha aumentado en {self.__damage_increase} puntos.")

#escuditoo
class ShieldItem(Item):
    def __init__(self, name, shield_amount):
        super().__init__(name, f"Añade {shield_amount} puntos de escudo")
        self.__shield_amount = shield_amount

    def apply(self, target):
        target.__shield += self.__shield_amount
        print(f"{target.name} ha ganado {self.shield_amount} puntos de escudo.")
##instaa kill 
# class DeathItem(Item):
#     def __init__(self, name):
#         super().__init__(name, "Causa muerte instantánea")

#     def apply(self, target):
#         target.health = 0
#         print(f"{target.name} ha sido eliminado instantáneamente.")


