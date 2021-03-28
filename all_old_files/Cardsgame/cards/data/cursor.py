from character import Character

class Cursor(Character):
    def __init__(self, file, size):
        super().__init__(file, size)

    def is_character(self):
        return False