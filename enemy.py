class Enemy:
    def __init__(self, name, health, shield, damage):
        self.name = name
        self.health = health
        self.shield = shield
        self.damage = damage

    def take_damage(self, amount):
        #Reduce el escudo y luego la vida en función del daño recibido.
        if self.shield > 0:
            remaining_damage = amount - self.shield
            self.shield = max(self.shield - amount, 0)
            if remaining_damage > 0:
                self.health = max(self.health - remaining_damage, 0)
        else:
            self.health = max(self.health - amount, 0)

    def attack(self):
        #Devuelve el daño que puede infligir el enemigo.
        return self.damage

    def is_alive(self):
        #Verifica si el enemigo sigue vivo.
        return self.health > 0

    def __str__(self):
        return (f"{self.name} - Vida: {self.health}, Escudo: {self.shield}, Daño: {self.damage}")
