from characters import Character
class Warrior(Character):
    #! Habilidad especial del luchador: ataque con aumento de daño
    def special_ability(self, enemy):
        damage = max(self.strength * 2.5 - enemy.defense, 0)
       # TODO enemy.FUNCION TOMAR DAÑO DE LOS ENEMIGOS(damage)
        print(f"{self.name} usó su habilidad especial y causó {damage} puntos de daño a {enemy.name}.")