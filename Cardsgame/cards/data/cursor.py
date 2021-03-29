from character import Character
import arcade 

class Cursor(arcade.Sprite):
    def __init__(self, file, size):
        super().__init__(file, size)

    def is_character(self):
        return False

    def next_image_idle(self):
        pass