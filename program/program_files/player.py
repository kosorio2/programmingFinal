from program_files.character import Character
import arcade

class Player(Character):
    def __init__(self, file, size):
        super().__init__(file, size)
        self.health = 100
        self.idle_animation = ["z_images/wraith/Wraith_01_Idle_000", "z_images/wraith/Wraith_01_Idle_001", "z_images/wraith/Wraith_01_Idle_002", "z_images/wraith/Wraith_01_Idle_003", "z_images/wraith/Wraith_01_Idle_004", "z_images/wraith/Wraith_01_Idle_005", "z_images/wraith/Wraith_01_Idle_006", "z_images/wraith/Wraith_01_Idle_007", "z_images/wraith/Wraith_01_Idle_008", "z_images/wraith/Wraith_01_Idle_009", "z_images/wraith/Wraith_01_Idle_010", "z_images/wraith/Wraith_01_Idle_011"]
        for i in range(0, 12):
            self.idle_animation[i] = arcade.load_texture(self.idle_animation[i] + ".png")
        self.attack_animation = ["z_images/wraith/Wraith_01_Attack_000", "z_images/wraith/Wraith_01_Attack_001", "z_images/wraith/Wraith_01_Attack_002", "z_images/wraith/Wraith_01_Attack_003", "z_images/wraith/Wraith_01_Attack_004", "z_images/wraith/Wraith_01_Attack_005", "z_images/wraith/Wraith_01_Attack_006", "z_images/wraith/Wraith_01_Attack_007", "z_images/wraith/Wraith_01_Attack_008", "z_images/wraith/Wraith_01_Attack_009", "z_images/wraith/Wraith_01_Attack_010", "z_images/wraith/Wraith_01_Attack_011"]
        for i in range(0, 12):
            self.attack_animation[i] = arcade.load_texture(self.attack_animation[i] + ".png")
        self.take_damage_animation = ["z_images/wraith/Wraith_01_Taunt_000", "z_images/wraith/Wraith_01_Taunt_001", "z_images/wraith/Wraith_01_Taunt_002", "z_images/wraith/Wraith_01_Taunt_003", "z_images/wraith/Wraith_01_Taunt_004", "z_images/wraith/Wraith_01_Taunt_005", "z_images/wraith/Wraith_01_Taunt_006", "z_images/wraith/Wraith_01_Taunt_007", "z_images/wraith/Wraith_01_Taunt_008", "z_images/wraith/Wraith_01_Taunt_009", "z_images/wraith/Wraith_01_Taunt_010", "z_images/wraith/Wraith_01_Taunt_012", "z_images/wraith/Wraith_01_Taunt_013", "z_images/wraith/Wraith_01_Taunt_014", "z_images/wraith/Wraith_01_Taunt_015", "z_images/wraith/Wraith_01_Taunt_015", "z_images/wraith/Wraith_01_Taunt_016", "z_images/wraith/Wraith_01_Taunt_017"]
        for i in range(0, 18):
            self.take_damage_animation[i] = arcade.load_texture(self.take_damage_animation[i] + ".png")
        self.defend_animation = ["z_images/wraith/Wraith_01_Taunt_000", "z_images/wraith/Wraith_01_Taunt_001", "z_images/wraith/Wraith_01_Taunt_002", "z_images/wraith/Wraith_01_Taunt_003", "z_images/wraith/Wraith_01_Taunt_004", "z_images/wraith/Wraith_01_Taunt_005", "z_images/wraith/Wraith_01_Taunt_006", "z_images/wraith/Wraith_01_Taunt_007", "z_images/wraith/Wraith_01_Taunt_008", "z_images/wraith/Wraith_01_Taunt_009", "z_images/wraith/Wraith_01_Taunt_010", "z_images/wraith/Wraith_01_Taunt_012", "z_images/wraith/Wraith_01_Taunt_013", "z_images/wraith/Wraith_01_Taunt_014", "z_images/wraith/Wraith_01_Taunt_015", "z_images/wraith/Wraith_01_Taunt_015", "z_images/wraith/Wraith_01_Taunt_016", "z_images/wraith/Wraith_01_Taunt_017"]
        for i in range(0, 18):
            self.defend_animation[i] = arcade.load_texture(self.defend_animation[i] + ".png")
        self.heal_animation = []
        self.death_animation = []
        for i in range(15):
            self.death_animation.append(arcade.load_texture(f"z_images/wraith/Wraith_01_Dying_00{i}.png"))

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

    