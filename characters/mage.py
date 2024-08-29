from characters import Character
class Mage(Character):
    #! Habilidad especial del mago: hechizo que ignora parte de la defensa del enemigo
    def cast_spell(self, enemy):
        damage = max(self.strength * 1.8 - enemy.defense * 0.5, 0)
       # TODO enemy.take_damage(damage)
        print(f"{self.name} lanzó un hechizo crítico y causó {damage} puntos de daño a {enemy.name}.")
