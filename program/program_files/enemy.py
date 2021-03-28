from program_files.character import Character
import random
import time

class Enemy(Character):
    def __init__(self, file, size):
        super().__init__(file, size)
        self.strength = 4
        self.intents = ["attack", "defend", "heal", "attack", "strengthen"]
        self.health = 100
        self.idle_animation = []
        self.attack_animation = []
        self.take_damage_animation = []
        self.death_animation = []

    def next_image_idle(self):
        pass
        

    def is_enemy(self):
        return True

    def get_health(self):
        return self.health

    def get_value(self):
        return random.randint(3, 6) * self.strength

    def get_strength(self):
        return self.strength

    def get_intent(self):
        number = random.randint(0, 4)
        return self.intents[number]
