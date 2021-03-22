import arcade
import random

class Card(arcade.Sprite):
    def __init__(self, file, size):
        super().__init__(file, size)
        number = random.randint(0, 2)
        card = ["Attack", "Defend", "Heal"]
        self.card_type = card[number]
        power = 10
        if number == 2:
            power = 5
        self.effect = [card[number], power]


    def effect_string(self):
        return f"{self.effect[0]}\n{self.effect[1]}"

    def get_effect(self):
        return self.effect