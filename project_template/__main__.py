import random
from rename.test import MyGame
# from Actor import Actor


def main():

    # enemy1 = Actor('Blade Vonner', 'Enemy1', ['Fire Ball', 'Sword Attack', 'Double Strike', 'Face Punch'],{'ATTACK': 5, 'DEFENSE':10})
    # enemy3 = Actor('Thorne Thornheart', 'Enemy1', ['Fire Ball', 'Sword Attack', 'Double Strike', 'Face Punch'],{'ATTACK':8, 'DEFENSE':12})

    # player = Actor('Kim', 'Player', ['Fire Ball', 'Sword Attack', 'Double Strike', 'Face Punch'],{'ATTACK':2, 'DEFENSE':2})
    


    # player.fight(enemy1) # Get them to fight

    def run_game():
        MyGame.main()

    if __name__ == "__main__":
        run_game()
