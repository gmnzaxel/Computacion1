from characters import Character
class Archer(Character):
    #! Habilidad especial del arquero: ataque a distancia con posibilidad de golpe crítico
    def shoot_arrow(self, enemy):
        critical_hit = 1.5 if self.level % 2 == 0 else 1  # Golpe crítico en niveles pares
        damage = max(self.strength * 1.3 * critical_hit - enemy.defense, 0)
        # TODO enemy.take_damage(damage)
        if critical_hit > 1:
            print(f"¡{self.name} realizó un golpe crítico!")
        print(f"{self.name} disparó una flecha causando {damage} puntos de daño a {enemy.name}.")
