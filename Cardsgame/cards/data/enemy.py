from cards.data.character import Character
import random
import arcade
import time 

class Enemy(Character):
    def __init__(self, file, size):
        super().__init__(file, size)
        self.strength = 1
        self.intents = ["attack", "defend", "heal", "attack", "strengthen"]
        self.health = 10
        self.idle_animation = ["z_images/minotaur/Minotaur_01_Idle_000", "z_images/minotaur/Minotaur_01_Idle_001", "z_images/minotaur/Minotaur_01_Idle_002", "z_images/minotaur/Minotaur_01_Idle_003", "z_images/minotaur/Minotaur_01_Idle_004", "z_images/minotaur/Minotaur_01_Idle_005", "z_images/minotaur/Minotaur_01_Idle_006", "z_images/minotaur/Minotaur_01_Idle_007", "z_images/minotaur/Minotaur_01_Idle_008", "z_images/minotaur/Minotaur_01_Idle_009", "z_images/minotaur/Minotaur_01_Idle_010", "z_images/minotaur/Minotaur_01_Idle_011"]
        self.attack_animation = ["z_images/minotaur/Minotaur_01_Attacking_000", "z_images/minotaur/Minotaur_01_Attacking_001", "z_images/minotaur/Minotaur_01_Attacking_002", "z_images/minotaur/Minotaur_01_Attacking_003", "z_images/minotaur/Minotaur_01_Attacking_004", "z_images/minotaur/Minotaur_01_Attacking_005", "z_images/minotaur/Minotaur_01_Attacking_006", "z_images/minotaur/Minotaur_01_Attacking_007", "z_images/minotaur/Minotaur_01_Attacking_008", "z_images/minotaur/Minotaur_01_Attacking_009", "z_images/minotaur/Minotaur_01_Attacking_010", "z_images/minotaur/Minotaur_01_Attacking_011"]
        self.take_damage_animation = ["z_images/minotaur/Minotaur_01_Taunt_000", "z_images/minotaur/Minotaur_01_Taunt_001", "z_images/minotaur/Minotaur_01_Taunt_002", "z_images/minotaur/Minotaur_01_Taunt_003", "z_images/minotaur/Minotaur_01_Taunt_004", "z_images/minotaur/Minotaur_01_Taunt_005", "z_images/minotaur/Minotaur_01_Taunt_006", "z_images/minotaur/Minotaur_01_Taunt_007", "z_images/minotaur/Minotaur_01_Taunt_008", "z_images/minotaur/Minotaur_01_Taunt_009", "z_images/minotaur/Minotaur_01_Taunt_010", "z_images/minotaur/Minotaur_01_Taunt_012", "z_images/minotaur/Minotaur_01_Taunt_013", "z_images/minotaur/Minotaur_01_Taunt_014", "z_images/minotaur/Minotaur_01_Taunt_015", "z_images/minotaur/Minotaur_01_Taunt_015", "z_images/minotaur/Minotaur_01_Taunt_016", "z_images/minotaur/Minotaur_01_Taunt_017"]
        self.defend_animation = ["z_images/minotaur/Minotaur_01_Taunt_000", "z_images/minotaur/Minotaur_01_Taunt_001", "z_images/minotaur/Minotaur_01_Taunt_002", "z_images/minotaur/Minotaur_01_Taunt_003", "z_images/minotaur/Minotaur_01_Taunt_004", "z_images/minotaur/Minotaur_01_Taunt_005", "z_images/minotaur/Minotaur_01_Taunt_006", "z_images/minotaur/Minotaur_01_Taunt_007", "z_images/minotaur/Minotaur_01_Taunt_008", "z_images/minotaur/Minotaur_01_Taunt_009", "z_images/minotaur/Minotaur_01_Taunt_010", "z_images/minotaur/Minotaur_01_Taunt_012", "z_images/minotaur/Minotaur_01_Taunt_013", "z_images/minotaur/Minotaur_01_Taunt_014", "z_images/minotaur/Minotaur_01_Taunt_015", "z_images/minotaur/Minotaur_01_Taunt_015", "z_images/minotaur/Minotaur_01_Taunt_016", "z_images/minotaur/Minotaur_01_Taunt_017"]
        self.death_animation = ["z_images/minotaur/Minotaur_01_Dying_000", "z_images/minotaur/Minotaur_01_Dying_001", "z_images/minotaur/Minotaur_01_Dying_002", "z_images/minotaur/Minotaur_01_Dying_003", "z_images/minotaur/Minotaur_01_Dying_004", "z_images/minotaur/Minotaur_01_Dying_005", "z_images/minotaur/Minotaur_01_Dying_006", "z_images/minotaur/Minotaur_01_Dying_007", "z_images/minotaur/Minotaur_01_Dying_008", "z_images/minotaur/Minotaur_01_Dying_009", "z_images/minotaur/Minotaur_01_Dying_010", "z_images/minotaur/Minotaur_01_Dying_011", "z_images/minotaur/Minotaur_01_Dying_012", "z_images/minotaur/Minotaur_01_Dying_013"]
        self.strengthen_animation = ["z_images/minotaur/Minotaur_01_Jump_Start_000", "z_images/minotaur/Minotaur_01_Jump_Start_001", "z_images/minotaur/Minotaur_01_Jump_Start_002", "z_images/minotaur/Minotaur_01_Jump_Start_003", "z_images/minotaur/Minotaur_01_Jump_Start_004", "z_images/minotaur/Minotaur_01_Jump_Start_005", "z_images/minotaur/Minotaur_01_Jump_Start_004", "z_images/minotaur/Minotaur_01_Jump_Start_003", "z_images/minotaur/Minotaur_01_Jump_Start_002", "z_images/minotaur/Minotaur_01_Jump_Start_001", "z_images/minotaur/Minotaur_01_Jump_Start_000"]
    def next_idle(self):
        if self.mode == 0:
            self.texture = arcade.load_texture(self.idle_animation[self.counter] + ".png", flipped_horizontally=True)
            if self.turn % 3 == 0:
                if self.counter >= 11:
                    self.counter = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 1:
            self.texture = arcade.load_texture(self.attack_animation[self.counter] + ".png", flipped_horizontally=True)
            if self.turn % 3 == 0:
                if self.counter >= 11:
                    self.counter = 0
                    self.mode = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 2:
            self.texture = arcade.load_texture(self.defend_animation[self.counter] + ".png", flipped_horizontally=True)
            if self.turn % 3 == 0:
                if self.counter >= 17:
                    self.counter = 0
                    self.mode = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 3:
            self.texture = arcade.load_texture(self.defend_animation[self.counter] + ".png", flipped_horizontally=True)
            if self.turn % 3 == 0:
                if self.counter >= 17:
                    self.counter = 0
                    self.mode = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 4:
            self.texture = arcade.load_texture(self.death_animation[self.counter] + ".png", flipped_horizontally=True)
            if self.turn % 1 == 0:
                if self.counter >= len(self.death_animation) - 1:
                    self.counter = len(self.death_animation) - 1
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 5:
            self.texture = arcade.load_texture(self.strengthen_animation[self.counter] + ".png", flipped_horizontally=True)
            if self.turn % 3 == 0:
                if self.counter >= len(self.strengthen_animation) - 1:
                    self.counter = 0
                    self.mode = 0
                else:
                    self.counter += 1
            self.turn += 1

    def set_attack(self):
        if self.health > 0:
            self.counter = 0
            self.mode = 1
        else: 
            self.set_dead()

    def set_defend(self):
        if self.health > 0:
            self.counter = 0
            self.mode = 2
        else: 
            self.set_dead()

    def set_heal(self):
        if self.health > 0:
            self.counter = 0
            self.mode = 3
        else: 
            self.set_dead()

    def set_strengthen(self):
        if self.health > 0:
            self.counter = 0
            self.mode = 5
        else:
            self.set_dead()

    def set_dead(self):
        if self.first_time:
            self.counter = 0
        self.first_time = False
        self.mode = 4

    def add_strength(self):
        self.strength += 2

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
