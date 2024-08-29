class Dungeon:
    def _init_(self):
        # Aquí creas a los enemigos y defines cuál es el enemigo actual
        self.current_enemy = Enemy("Goblin", 50, 15, 5)

class Enemy:
    def _init_(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense