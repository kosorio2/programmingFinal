import arcade
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750

class Card(arcade.Sprite):
    def __init__(self, file, size, card_number):
        super().__init__(file, size)
        self.card_number = card_number
        if card_number <= 22:
            number = 0
        elif card_number <= 45:
            number = 1
        else:
            number = 2
        card = ["Attack", "Defend", "Heal"]
        self.card_type = card[number]
        power = random.randint(5, 10)
        if number == 2:
            power = random.randint(3, 7)
        self.effect = [card[number], power]
        self.in_hand = False
        if self.effect[0] == "Attack":
            self.texture = arcade.load_texture("z_images/card11.png")
        elif self.effect[0] == "Defend":
            self.texture = arcade.load_texture("z_images/card1.png")
        elif self.effect[0] == "Heal":
            self.texture = arcade.load_texture("z_images/card6.png")

    def effect_string(self):
        return f"{self.effect[0]}\n{self.effect[1]}"

    def get_card_number(self):
        return self.card_number

    def get_effect(self):
        return self.effect

    def in_hand(self):
        self.in_hand = True

    def out_of_hand(self):
        self.in_hand = False
    
    def set_slot(self, slot):
        self.slot = slot
        if slot == 1:
            self.center_x = 200
            self.center_y = SCREEN_HEIGHT - 90

        elif slot == 2:
            self.center_x = 290
            self.center_y = SCREEN_HEIGHT - 90

        elif slot == 3:
            self.center_x = 380
            self.center_y = SCREEN_HEIGHT - 90

        elif slot == 4:
            self.center_x = 470
            self.center_y = SCREEN_HEIGHT - 90

        elif slot == 5:
            self.center_x = 560
            self.center_y = SCREEN_HEIGHT - 90

    def get_slot(self):
        return self.slot
        