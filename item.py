from constant import (
    HEALING_ITEM_MESSAGE,
    DAMAGE_BOOST_ITEM_MESSAGE,
    SHIELD_ITEM_MESSAGE,
    STRENGTH_DECREASE_ITEM_MESSAGE,
    DEFENSE_DECREASE_ITEM_MESSAGE,
    SHIELD_DECREASE_ITEM_MESSAGE,
    DAMAGE_ITEM_MESSAGE,
    HEALING_ITEM_DESCRIPTION,
    DAMAGE_BOOST_ITEM_DESCRIPTION,
    SHIELD_ITEM_DESCRIPTION,
    STRENGTH_DECREASE_ITEM_DESCRIPTION,
    DEFENSE_DECREASE_ITEM_DESCRIPTION,
    SHIELD_DECREASE_ITEM_DESCRIPTION,
    DAMAGE_ITEM_DESCRIPTION

)

class Item:
    def __init__(self, name, effect):
        self.__name = name
        self.__effect = effect
        self.__position = (0, 0)

    def __str__(self):
        return f"{self.__name} - Efecto: {self.__effect}"

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position

# curan
class HealingItem(Item):
    def __init__(self, name, healing_amount):
        super().__init__(name, HEALING_ITEM_DESCRIPTION.format(healing_amount))
        self.__healing_amount = healing_amount

    def apply(self, target):
        # Verifica si el personaje esta vivo antes de curarlo
        if target.get_health() > 0:
            target.set_health(target.get_health() + self.__healing_amount)
            print(HEALING_ITEM_MESSAGE.format(target.get_name(), self.__healing_amount))

# aumenta daño 
class DamageBoostItem(Item):
    def __init__(self, name, damage_increase):
        super().__init__(name, DAMAGE_BOOST_ITEM_DESCRIPTION.format(damage_increase))
        self.__damage_increase = damage_increase

    def apply(self, target):
        target.set_strength(target.get_strength() + self.__damage_increase)
        print(DAMAGE_BOOST_ITEM_MESSAGE.format(target.get_name(), self.__damage_increase))

# añade escudo 
class ShieldItem(Item):
    def __init__(self, name, shield_amount):
        super().__init__(name, SHIELD_ITEM_DESCRIPTION.format(shield_amount))
        self.__shield_amount = shield_amount

    def apply(self, target):
        target.set_defense(target.get_defense() + self.__shield_amount)
        print(SHIELD_ITEM_MESSAGE.format(target.get_name(), self.__shield_amount))

# disminue  fuerza 
class StrengthDecreaseItem(Item):
    def __init__(self, name, strength_decrease):
        super().__init__(name, STRENGTH_DECREASE_ITEM_DESCRIPTION.format(strength_decrease))
        self.__strength_decrease = strength_decrease

    def apply(self, target):
        target.set_strength(target.get_strength() - self.__strength_decrease)
        print(STRENGTH_DECREASE_ITEM_MESSAGE.format(target.get_name(), self.__strength_decrease))

# disminue defensa 
class DefenseDecreaseItem(Item):
    def __init__(self, name, defense_decrease):
        super().__init__(name, DEFENSE_DECREASE_ITEM_DESCRIPTION.format(defense_decrease))
        self.__defense_decrease = defense_decrease

    def apply(self, target):
        target.set_defense(target.get_defense() - self.__defense_decrease)
        print(DEFENSE_DECREASE_ITEM_MESSAGE.format(target.get_name(), self.__defense_decrease))

# disminue escudo 
class ShieldDecreaseItem(Item):
    def __init__(self, name, shield_decrease):
        super().__init__(name, SHIELD_DECREASE_ITEM_DESCRIPTION.format(shield_decrease))
        self.__shield_decrease = shield_decrease

    def apply(self, target):
        target.set_defense(target.get_defense() - self.__shield_decrease)
        print(SHIELD_DECREASE_ITEM_MESSAGE.format(target.get_name(), self.__shield_decrease))

# daño al personaje
class DamageItem(Item):
    def __init__(self, name, damage_amount):
        super().__init__(name, DAMAGE_ITEM_DESCRIPTION.format(damage_amount))
        self.__damage_amount = damage_amount

    def apply(self, target):
        target.set_health(target.get_health() - self.__damage_amount)
        print(DAMAGE_ITEM_MESSAGE.format(target.get_name(), self.__damage_amount))