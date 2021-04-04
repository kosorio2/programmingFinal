from cards.data.character import Character
import random
import arcade
import time 

class Enemy(Character):
    def __init__(self, file, size):
        super().__init__(file, size)
        self.strength = random.randint(1,3)
        which_enemy = str(random.randint(1, 3))
        self.intents = ["attack", "defend", "heal", "attack", "strengthen"]
        self.health = random.randint(30,50)
        self.max_health = self.health + 5
        self.idle_animation = [f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_000", f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_001", f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_002", f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_003", f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_004", f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_005", f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_006", f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_007", f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_008", f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_009", f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_010", f"z_images/minotaur/Minotaur_0{which_enemy}_Idle_011"]
        for i in range(0, 12):
            self.idle_animation[i] = arcade.load_texture(self.idle_animation[i] + ".png", flipped_horizontally=True)
        self.attack_animation = [f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_000", f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_001", f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_002", f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_003", f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_004", f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_005", f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_006", f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_007", f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_008", f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_009", f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_010", f"z_images/minotaur/Minotaur_0{which_enemy}_Attacking_011"]
        for i in range(0, 12):
            self.attack_animation[i] = arcade.load_texture(self.attack_animation[i] + ".png", flipped_horizontally=True)
        self.take_damage_animation = [f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_000", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_001", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_002", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_003", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_004", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_005", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_006", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_007", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_008", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_009", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_010", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_012", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_013", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_014", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_015", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_015", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_016", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_017"]
        for i in range(0, 18):
            self.take_damage_animation[i] = arcade.load_texture(self.take_damage_animation[i] + ".png", flipped_horizontally=True)
        self.defend_animation = [f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_000", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_001", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_002", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_003", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_004", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_005", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_006", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_007", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_008", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_009", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_010", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_012", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_013", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_014", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_015", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_015", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_016", f"z_images/minotaur/Minotaur_0{which_enemy}_Taunt_017"]
        for i in range(0, 18):
            self.defend_animation[i] = arcade.load_texture(self.defend_animation[i] + ".png", flipped_horizontally=True)
        self.death_animation = [f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_000", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_001", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_002", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_003", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_004", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_005", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_006", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_007", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_008", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_009", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_010", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_011", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_012", f"z_images/minotaur/Minotaur_0{which_enemy}_Dying_013"]
        for i in range(0, 14):
            self.death_animation[i] = arcade.load_texture(self.death_animation[i] + ".png", flipped_horizontally=True)
        self.strengthen_animation = [f"z_images/minotaur/Minotaur_0{which_enemy}_Jump_Start_000", f"z_images/minotaur/Minotaur_0{which_enemy}_Jump_Start_001", f"z_images/minotaur/Minotaur_0{which_enemy}_Jump_Start_002", f"z_images/minotaur/Minotaur_0{which_enemy}_Jump_Start_003", f"z_images/minotaur/Minotaur_0{which_enemy}_Jump_Start_004", f"z_images/minotaur/Minotaur_0{which_enemy}_Jump_Start_005", f"z_images/minotaur/Minotaur_0{which_enemy}_Jump_Start_004", f"z_images/minotaur/Minotaur_0{which_enemy}_Jump_Start_003", f"z_images/minotaur/Minotaur_0{which_enemy}_Jump_Start_002", f"z_images/minotaur/Minotaur_0{which_enemy}_Jump_Start_001", f"z_images/minotaur/Minotaur_0{which_enemy}_Jump_Start_000"]
        for i in range(0, 11):
            self.strengthen_animation[i] = arcade.load_texture(self.strengthen_animation[i] + ".png", flipped_horizontally=True)

    def next_idle(self):
        if self.mode == 0:
            self.texture = self.idle_animation[self.counter]
            if self.turn % 3 == 0:
                if self.counter >= 11:
                    self.counter = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 1:
            self.texture = self.attack_animation[self.counter]
            if self.turn % 3 == 0:
                if self.counter >= 11:
                    self.counter = 0
                    self.mode = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 2:
            self.texture = self.defend_animation[self.counter]
            if self.turn % 3 == 0:
                if self.counter >= 17:
                    self.counter = 0
                    self.mode = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 3:
            self.texture = self.defend_animation[self.counter]
            if self.turn % 3 == 0:
                if self.counter >= 17:
                    self.counter = 0
                    self.mode = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 4:
            self.texture = self.death_animation[self.counter]
            if self.turn % 1 == 0:
                if self.counter >= len(self.death_animation) - 1:
                    self.counter = len(self.death_animation) - 1
                    self.kill()
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 5:
            self.texture = self.strengthen_animation[self.counter]
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
