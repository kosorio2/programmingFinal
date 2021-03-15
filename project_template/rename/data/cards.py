import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 2.0
SPRITE_SCALING_COIN = .25
COIN_COUNT = 0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins Example"


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

        # Variables that will hold sprite lists
        self.character_list = None
        self.coin_list = None
        self.deck = None
        self.held_cards_original_position = None
        self.held_cards = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

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

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.enemy_sprite = arcade.Sprite(":resources:images/animated_characters/robot/robot_fall.png", 
                                          SPRITE_SCALING_PLAYER)
        self.enemy_sprite.center_x = SCREEN_WIDTH - 90
        self.enemy_sprite.center_y = SCREEN_HEIGHT / 2
        self.character_list.append(self.enemy_sprite)

        self.protagonist_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", 
                                                SPRITE_SCALING_PLAYER)
        self.protagonist_sprite.center_x = 90
        self.protagonist_sprite.center_y = SCREEN_HEIGHT/2
        self.character_list.append(self.protagonist_sprite)

        # Create the coins
        j = 0
        for i in starting_hand:
            card = arcade.Sprite(":resources:images/cards/card" + str(i) + ".png", 0.5)
            card.center_x = 200 + j
            card.center_y = 90
            j += 90
            self.deck.append(card)
        
        for i in range(5):
            self.additional_cards.append(self.choose_number(self.usedNumbers, 68))
        
        for i in self.additional_cards:
            card = arcade.Sprite(":resources:images/cards/card" + str(i) + ".png", 0.5)
            card.center_x = 90
            card.center_y = 70
            self.deck.append(card)

        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite(":resources:images/items/coinGold.png",
                                 SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerLife1_orange.png",
                                    SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.character_list.append(self.player_sprite)

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

        print(hit_list)

        if len(hit_list) > 1:
            reset_position = False

        if reset_position:
            # Where-ever we were dropped, it wasn't valid. Reset the each card's position
            # to its original spot.
            for pile_index, card in enumerate(self.held_cards):
                card.position = self.held_cards_original_position[pile_index]
        else:
            for card in self.held_cards:
                card.center_x = SCREEN_WIDTH - 90
                card.center_y = 90

        # We are no longer holding cards
        self.held_cards = []

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.character_list.draw()
        self.deck.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
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
                card.center_y = 70
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