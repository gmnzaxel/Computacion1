class Enemy:
    def __init__(self, name, health, shield, damage):
        self.__name = name
        self.__health = health
        self.__shield = shield
        self.__damage = damage

    def take_damage(self, amount):
        #Reduce el escudo y luego la vida en función del daño recibido.
        if self.__shield > 0:
            remaining_damage = amount - self.shield
            self.__shield = max(self.__shield - amount, 0)
            if remaining_damage > 0:
                self.__health = max(self.__health - remaining_damage, 0)
        else:
            self.__health = max(self.__health - amount, 0)

    def attack(self):
        #Devuelve el daño que puede infligir el enemigo.
        return self.__damage

    def is_alive(self):
        #Verifica si el enemigo sigue vivo.
        return self.__health > 0

    def __str__(self):
        return (f"{self.__name} - Vida: {self.__health}, Escudo: {self.__shield}, Daño: {self.__damage}")
