from game import Game
from background_sound import MySound
import arcade

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
    
    def main():
        """ Main method """
        window = MySound()
        window.setup()
        arcade.run()

    if __name__ == "__main__":
        main()