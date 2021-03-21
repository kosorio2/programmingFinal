from program_files.character import Character

class Player(Character):
    def __init__(self, file, size):
        super().__init__(file, size)
        self.health = 100

    def get_health(self):
        return self.health

    