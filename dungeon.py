class Dungeon:
    def _init_(self):
        # Acá creas a los enemigos y definís cuál es el enemigo actual
        self.current_enemy = Enemy("Goblin", 50, 15, 5)

class Enemy:
    def _init_(self, name, health, strength, defense):
        self.__name = name
        self.__health = health
        self.__strength = strength
        self.__defense = defense
