from cards.data.character import Character
import arcade
import random



class Player(Character):
    def __init__(self, file, size):
        super().__init__(file, size)
        self.health = 100
        which_character = random.randint(1, 3)
        self.idle_animation = [f"z_images/wraith/Wraith_0{which_character}_Idle_000", f"z_images/wraith/Wraith_0{which_character}_Idle_001", f"z_images/wraith/Wraith_0{which_character}_Idle_002", f"z_images/wraith/Wraith_0{which_character}_Idle_003", f"z_images/wraith/Wraith_0{which_character}_Idle_004", f"z_images/wraith/Wraith_0{which_character}_Idle_005", f"z_images/wraith/Wraith_0{which_character}_Idle_006", f"z_images/wraith/Wraith_0{which_character}_Idle_007", f"z_images/wraith/Wraith_0{which_character}_Idle_008", f"z_images/wraith/Wraith_0{which_character}_Idle_009", f"z_images/wraith/Wraith_0{which_character}_Idle_010", f"z_images/wraith/Wraith_0{which_character}_Idle_011"]
        for i in range(0, 12):
            self.idle_animation[i] = arcade.load_texture(self.idle_animation[i] + ".png")
        self.attack_animation = [f"z_images/wraith/Wraith_0{which_character}_Attack_000", f"z_images/wraith/Wraith_0{which_character}_Attack_001", f"z_images/wraith/Wraith_0{which_character}_Attack_002", f"z_images/wraith/Wraith_0{which_character}_Attack_003", f"z_images/wraith/Wraith_0{which_character}_Attack_004", f"z_images/wraith/Wraith_0{which_character}_Attack_005", f"z_images/wraith/Wraith_0{which_character}_Attack_006", f"z_images/wraith/Wraith_0{which_character}_Attack_007", f"z_images/wraith/Wraith_0{which_character}_Attack_008", f"z_images/wraith/Wraith_0{which_character}_Attack_009", f"z_images/wraith/Wraith_0{which_character}_Attack_010", f"z_images/wraith/Wraith_0{which_character}_Attack_011"]
        for i in range(0, 12):
            self.attack_animation[i] = arcade.load_texture(self.attack_animation[i] + ".png")
        self.take_damage_animation = [f"z_images/wraith/Wraith_0{which_character}_Taunt_000", f"z_images/wraith/Wraith_0{which_character}_Taunt_001", f"z_images/wraith/Wraith_0{which_character}_Taunt_002", f"z_images/wraith/Wraith_0{which_character}_Taunt_003", f"z_images/wraith/Wraith_0{which_character}_Taunt_004", f"z_images/wraith/Wraith_0{which_character}_Taunt_005", f"z_images/wraith/Wraith_0{which_character}_Taunt_006", f"z_images/wraith/Wraith_0{which_character}_Taunt_007", f"z_images/wraith/Wraith_0{which_character}_Taunt_008", f"z_images/wraith/Wraith_0{which_character}_Taunt_009", f"z_images/wraith/Wraith_0{which_character}_Taunt_010", f"z_images/wraith/Wraith_0{which_character}_Taunt_012", f"z_images/wraith/Wraith_0{which_character}_Taunt_013", f"z_images/wraith/Wraith_0{which_character}_Taunt_014", f"z_images/wraith/Wraith_0{which_character}_Taunt_015", f"z_images/wraith/Wraith_0{which_character}_Taunt_015", f"z_images/wraith/Wraith_0{which_character}_Taunt_016", f"z_images/wraith/Wraith_0{which_character}_Taunt_017"]
        for i in range(0, 18):
            self.take_damage_animation[i] = arcade.load_texture(self.take_damage_animation[i] + ".png")
        self.defend_animation = [f"z_images/wraith/Wraith_0{which_character}_Taunt_000", f"z_images/wraith/Wraith_0{which_character}_Taunt_001", f"z_images/wraith/Wraith_0{which_character}_Taunt_002", f"z_images/wraith/Wraith_0{which_character}_Taunt_003", f"z_images/wraith/Wraith_0{which_character}_Taunt_004", f"z_images/wraith/Wraith_0{which_character}_Taunt_005", f"z_images/wraith/Wraith_0{which_character}_Taunt_006", f"z_images/wraith/Wraith_0{which_character}_Taunt_007", f"z_images/wraith/Wraith_0{which_character}_Taunt_008", f"z_images/wraith/Wraith_0{which_character}_Taunt_009", f"z_images/wraith/Wraith_0{which_character}_Taunt_010", f"z_images/wraith/Wraith_0{which_character}_Taunt_012", f"z_images/wraith/Wraith_0{which_character}_Taunt_013", f"z_images/wraith/Wraith_0{which_character}_Taunt_014", f"z_images/wraith/Wraith_0{which_character}_Taunt_015", f"z_images/wraith/Wraith_0{which_character}_Taunt_015", f"z_images/wraith/Wraith_0{which_character}_Taunt_016", f"z_images/wraith/Wraith_0{which_character}_Taunt_017"]
        for i in range(0, 18):
            self.defend_animation[i] = arcade.load_texture(self.defend_animation[i] + ".png")
        self.heal_animation = []
        self.death_animation = []
        for i in range(15):
            self.death_animation.append(arcade.load_texture(f"z_images/wraith/Wraith_0{which_character}_Dying_00{i}.png"))

    def get_health(self):
        return self.health

    def next_idle(self):
        if self.mode == 0:
            self.texture = self.idle_animation[self.counter]
            if self.turn % 2 == 0:
                if self.counter >= 11:
                    self.counter = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 1:
            self.texture = self.attack_animation[self.counter]
            if self.turn % 2 == 0:
                if self.counter >= 11:
                    self.counter = 0
                    self.mode = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 2:
            self.texture = self.defend_animation[self.counter]
            if self.turn % 2 == 0:
                if self.counter >= 17:
                    self.counter = 0
                    self.mode = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 3:
            self.texture = self.defend_animation[self.counter]
            if self.turn % 2 == 0:
                if self.counter >= 17:
                    self.counter = 0
                    self.mode = 0
                else:
                    self.counter += 1
            self.turn += 1

        elif self.mode == 4:
            self.texture = self.death_animation[self.counter]
            if self.turn % 1 == 0:
                if self.counter >= 14:
                    self.counter = 14
                else:
                    self.counter += 1
            self.turn += 1

    def set_attack(self):
        if self.health > 0:
            self.counter = 0
            self.mode = 1
        else: 
            self.set_dead

    def set_defend(self):
        if self.health > 0:
            self.counter = 0
            self.mode = 2
        else: 
            self.set_dead

    def set_heal(self):
        if self.health > 0:
            self.counter = 0
            self.mode = 3
        else: 
            self.set_dead

    def set_dead(self):
        if self.first_time:
            self.counter = 0
        self.first_time = False
        self.mode = 4