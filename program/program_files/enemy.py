from program_files.character import Character
import random

class Enemy(Character):
    def __init__(self, file, size):
        super().__init__(file, size)
        self.strength = 4
        self.intents = ["attack", "defend", "heal"]
        self.health = 100

    def is_enemy(self):
        return True

    def get_health(self):
        return self.health

    def get_value(self):
        return random.randint(3, 6) * self.strength

    def get_strength(self):
        return self.strength

    def get_intent(self):
        number = random.randint(0, 2)
        return self.intents[number]
