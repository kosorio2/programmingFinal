from program_files.card import Card
from program_files.cursor import Cursor
from program_files.enemy import Enemy
from program_files.player import Player

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 2.0
SPRITE_SCALING_CURSOR = .5
SPRITE_SCALING_COIN = .25
COIN_COUNT = 2

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Luck of the Draw"


class MyGame(arcade.Window):
    """ Our custom Window Class"""
    def choose_number(self, usedNumbers, number_range):
        is_number_new = False
        while is_number_new == False:
            whichOne = random.randint(0, number_range)
            for i in range(0, len(usedNumbers)):
                if usedNumbers[i] == whichOne:
                    is_number_new = False
                    break
                else:
                    is_number_new = True
        usedNumbers.append(whichOne)
        return whichOne

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # self.card = Card()
        # self.cursor = Cursor()
        # self.enemy = Enemy()
        # self.player = Player()
        self.game_over = False

        # Variables that will hold sprite lists
        self.character_list = None
        self.coin_list = None
        self.deck = None
        self.held_cards_original_position = None
        self.held_cards = None
        self.cards_played = 0
        self.already_went = 0

        # Set up the player info
        self.cursor_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        self.background = None
        self.game_over_screen = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.coin_list = arcade.SpriteList()
        self.deck = arcade.SpriteList()
        self.character_list = arcade.SpriteList()
        self.usedNumbers = [0]
        starting_hand = []
        self.additional_cards = []
        self.held_cards_original_position = []
        self.held_cards = []
        for i in range(5):
            starting_hand.append(self.choose_number(self.usedNumbers, 68))
        print(starting_hand)

        self.background = arcade.load_texture("z_images/background.png")
        self.game_over_screen = arcade.load_texture("z_images/game_over.png")

        # Create the coins
        j = 0
        for i in starting_hand:
            card = Card("z_images/card" + str(i) + ".png", 0.5)
            card.center_x = 200 + j
            card.center_y = SCREEN_HEIGHT - 90
            j += 90
            self.deck.append(card)
        
        for i in range(5):
            self.additional_cards.append(self.choose_number(self.usedNumbers, 68))
        
        for i in self.additional_cards:
            card = Card("z_images/card" + str(i) + ".png", 0.5)
            card.center_x = 90
            card.center_y = SCREEN_HEIGHT - 70
            self.deck.append(card)

        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            if i == 1:
                coin = arcade.Sprite("z_images/card11.png", 0.54)
                coin.center_x = SCREEN_WIDTH - 90
                coin.center_y = SCREEN_HEIGHT - 70
            else:
                coin = arcade.Sprite("z_images/card1.png", 0.54)
                coin.center_x = 90
                coin.center_y = SCREEN_HEIGHT - 70

            # Add the coin to the lists
            self.coin_list.append(coin)

        self.enemy_sprite = Enemy("z_images/Enemy.png", SPRITE_SCALING_CURSOR)
        self.enemy_sprite.center_x = SCREEN_WIDTH - 180
        self.enemy_sprite.center_y = 180
        self.character_list.append(self.enemy_sprite)

        self.protagonist_sprite = Player("z_images/maleAdventurer_idle.png", SPRITE_SCALING_PLAYER)
        self.protagonist_sprite.center_x = 90
        self.protagonist_sprite.center_y = 180
        self.character_list.append(self.protagonist_sprite)

        self.cursor_sprite = Cursor("z_images/Cursor.png",
                                SPRITE_SCALING_CURSOR)
        self.cursor_sprite.center_x = 50
        self.cursor_sprite.center_y = 50
        self.character_list.append(self.cursor_sprite)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of cards we've clicked on
        cards = arcade.get_sprites_at_point((x, y), self.deck)

        # Have we clicked on a card?
        if len(cards) > 0:

            # Might be a stack of cards, get the top one
            primary_card = cards[-1]

            # All other cases, grab the face-up card we are clicking on
            self.held_cards = [primary_card]
            # Save the position
            self.held_cards_original_position = [self.held_cards[0].position]
            # Put on top in drawing order



    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """

        # If we don't have any cards, who cares
        if len(self.held_cards) == 0:
            return

        reset_position = True

        hit_list = arcade.check_for_collision_with_list(self.held_cards[0], self.character_list)

        effect = self.held_cards[0].get_effect()
        

        if len(hit_list) > 1:
            reset_position = False

        if reset_position:
            # Where-ever we were dropped, it wasn't valid. Reset each card's position
            # to its original spot.
            for pile_index, card in enumerate(self.held_cards):
                card.position = self.held_cards_original_position[pile_index]
        else:
            for card in self.held_cards:
                card.center_x = SCREEN_WIDTH - 90
                card.center_y = SCREEN_HEIGHT - 90
            for character in hit_list:
                if effect[0] == "Attack":
                    character.do_damage(effect[1])
                    self.cards_played = self.cards_played + 1
                    self.already_went = 1
                    print(self.already_went)
                elif effect[0] == "Defend" and character.is_enemy() == False:
                    character.add_shield(effect[1])
                    self.cards_played = self.cards_played + 1
                    self.already_went = 1
                elif effect[0] == "Heal" and character.is_enemy() == False:
                    character.add_health(effect[1])
                    self.cards_played = self.cards_played + 1
                    self.already_went = 1
                else:
                    for pile_index, card in enumerate(self.held_cards):
                        card.position = self.held_cards_original_position[pile_index]

        # We are no longer holding cards
        self.held_cards = []

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.coin_list.draw()
        self.deck.draw()
        self.character_list.draw()
        
        for card in self.deck:
            output = card.effect_string()
            arcade.draw_text(output, card.center_x - 20, card.center_y - 80, arcade.color.BLACK, 14)
        # Put the text on the screen.
        for character in self.character_list:
            if character.is_character() == True:
                output = f"Health: {character.get_health()}\nShield: {character.get_shield()}"
                arcade.draw_text(output, character.center_x - 40, character.center_y + 125, arcade.color.WHITE, 14)
        if self.game_over == True:
            arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y

        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.deck.update()

        # Generate a list of all sprites that collided with the player.
        cards_hit_list = arcade.check_for_collision_with_list(self.deck[0], self.deck)

        if len(cards_hit_list) == len(self.deck) - 1:
            for card in cards_hit_list:
                card.center_x = 90
                card.center_y = SCREEN_HEIGHT - 70

        for character in self.character_list:
            if character.get_health() <= 0:
                self.game_over = True
        

        if self.cards_played % 3 == 0 and self.cards_played > 0 and self.already_went == 1:
            self.enemy_sprite.reset_shield()
            self.already_went = self.already_went + 1
            # print(self.already_went)
            intent = self.enemy_sprite.get_intent()
            if intent == "attack":
                self.protagonist_sprite.do_damage(self.enemy_sprite.get_value())
            elif intent == "defend":
                self.enemy_sprite.add_shield(self.enemy_sprite.get_value())
            elif intent == "heal":
                self.enemy_sprite.add_health(self.enemy_sprite.get_value())
            self.protagonist_sprite.reset_shield()
            # for card in self.deck:
            #     self.choose_number(self.deck, 68)    
        
        # Loop through each colliding sprite, remove it, and add to the score.
        # for coin in coins_hit_list:
        #     coin.remove_from_sprite_lists()
        #     self.score += 1


    def main():
        """ Main method """
        window = MyGame()
        window.setup()
        arcade.run()


    if __name__ == "__main__":
        main()