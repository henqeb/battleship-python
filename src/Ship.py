class Ship:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self):
        self.hp -= 1

    def is_alive(self):
        return self.hp < 1
