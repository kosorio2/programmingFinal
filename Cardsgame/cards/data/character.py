import arcade

class Character(arcade.Sprite):
    def __init__(self, file, size):
        super().__init__(file, size)
        self.health = 100
        self.shield = 0
        self.idle_animation = []
        self.attack_animation = []
        self.take_damage_animation = []
        self.death_animation = []
        self.next_animation = 0
        self.mode = 0
        self.counter = 0
        self.turn = 0
        self.first_time = True

    def next_image_idle(self):
        self.filename = self.idle_animation[self.next_animation % len(self.idle_animation)]
        self.next_animation += 1

    def is_enemy(self):
        return False

    def set_health(self, new_value):
        self.health = new_value

    def is_character(self):
        return True

    def get_health(self):
        return self.health

    def add_health(self, additional_health):
        self.health = self.health + additional_health

    def get_shield(self):
        return self.shield

    def reset_shield(self):
        self.shield = 0
    
    def add_shield(self, amount):
        self.shield = self.shield + amount

    def do_damage(self, damage):
        original_damage = damage
        damage = damage - self.shield
        self.shield = self.shield - original_damage
        if self.shield < 0:
            self.shield = 0
        if damage < 0:
            damage = 0

        self.health = self.health - damage