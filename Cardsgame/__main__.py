from cards.data.menuGame import Game
from cards.data.background_sound import MySound
import arcade

g = Game()

g.setup()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
    # MySound.music.stop()
    # while g.setup():