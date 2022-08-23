from abc import ABC, abstractmethod


class Ship(ABC):

    def __init__(self, hp):
        self.hp = hp

    @property
    def get_hp(self):
        return self.hp

    def take_damage(self):
        self.hp -= 1

    def ship_is_alive(self):
        return self.hp < 1


class Carrier(Ship):
    """Carrier instance of a ship. Has 5 HP."""

    def __init__(self, hp):
        super().__init__(hp)
        self.name = "Carrier"


class Battleship(Ship):
    def __init__(self, hp):
        super().__init__(hp)
        self.name = "Battleship"


class Cruiser(Ship):
    def __init__(self, hp):
        super().__init__(hp)
        self.name = "Cruiser"


class Submarine(Ship):
    def __init__(self, hp):
        super().__init__(hp)
        self.name = "Submarine"


class Destroyer(Ship):
    def __init__(self, hp):
        super().__init__(hp)
        self.name = "Destroyer"
