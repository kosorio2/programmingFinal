from cards.data.card import Card
from cards.data.cursor import Cursor
from cards.data.enemy import Enemy
from cards.data.player import Player
from cards.data.background_sound import MySound

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 1.0
ENEMY_SPRITE_SCALING = 0.85
SPRITE_SCALING_CURSOR = .5
SPRITE_SCALING_COIN = .25
COIN_COUNT = 2

SCREEN_WIDTH = 1700
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
        self.game_over = False

        # Variables that will hold sprite lists
        self.character_list = None
        self.cursor_list = None
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

        #Play sound effects
        self.attackSound = arcade.load_sound("Cardsgame/cards/data/sounds/attackSound.wav")
        self.defendSound = arcade.load_sound("Cardsgame/cards/data/sounds/defendSound.wav")
        self.healSound = arcade.load_sound("Cardsgame/cards/data/sounds/healSound.wav")


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.coin_list = arcade.SpriteList()
        self.deck = arcade.SpriteList()
        self.character_list = arcade.SpriteList()
        self.cursor_list = arcade.SpriteList()


        self.usedNumbers = [0]
        self.deck_numbers = []
        self.empty_slots = [1, 2, 3, 4, 5]
        self.used_cards = []
        starting_hand = []
        self.additional_cards = []
        self.held_cards_original_position = []
        self.held_cards = []
        for i in range(5):
            number = self.choose_number(self.usedNumbers, 68)
            starting_hand.append(number)
            self.deck_numbers.append(number)
        print(starting_hand)

        self.background = arcade.load_texture("z_images/background.png")
        self.game_over_screen = arcade.load_texture("z_images/game_over.png")

        j = 1
        for i in starting_hand:
            card = Card("z_images/card" + str(i) + ".png", 0.5, i)
            card.set_slot(j)
            j += 1
            self.deck.append(card)
        
        for i in range(10):
            number = self.choose_number(self.usedNumbers, 68)
            self.additional_cards.append(number)
            self.deck_numbers.append(number)
        
        # for i in self.additional_cards:
        #     card = Card("z_images/card" + str(i) + ".png", 0.5, i)
        #     card.center_x = 90
        #     card.center_y = SCREEN_HEIGHT - 70
        #     self.deck.append(card)

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

        self.enemy_sprite = Enemy("z_images/Enemy.png", ENEMY_SPRITE_SCALING)
        self.enemy_sprite.center_x = SCREEN_WIDTH - 300
        self.enemy_sprite.center_y = 250
        self.character_list.append(self.enemy_sprite)

        self.protagonist_sprite = Player("z_images/maleAdventurer_idle.png", SPRITE_SCALING_PLAYER)
        self.protagonist_sprite.center_x = 180
        self.protagonist_sprite.center_y = 180
        self.character_list.append(self.protagonist_sprite)

        self.cursor_sprite = Cursor("z_images/Cursor.png",
                                SPRITE_SCALING_CURSOR)
        self.cursor_sprite.center_x = 50
        self.cursor_sprite.center_y = 50
        self.cursor_list.append(self.cursor_sprite)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of cards we've clicked on
        cards = arcade.get_sprites_at_point((x, y), self.deck)

        # Have we clicked on a card?
        if len(cards) > 0:

            primary_card = cards[-1]

            # All other cases, grab the face-up card we are clicking on
            self.held_cards = [primary_card]
            # Save the position
            self.held_cards_original_position = [self.held_cards[0].position]
            # Put on top in drawing order



    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user releases a pressed mouse button. """

        # If we don't have any cards, who cares
        if len(self.held_cards) == 0:
            return

        reset_position = True

        hit_list = arcade.check_for_collision_with_list(self.held_cards[0], self.character_list)
        print(hit_list)
        effect = self.held_cards[0].get_effect()
        

        if len(hit_list) > 0 and self.protagonist_sprite.get_health() > 0:
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
            character = hit_list[0]
            if effect[0] == "Attack" and character.is_enemy():
                self.protagonist_sprite.set_attack()
                arcade.play_sound(self.attackSound)  
                character.do_damage(effect[1])
                self.cards_played = self.cards_played + 1
                self.already_went = 1

                self.used_cards.append(self.held_cards[0].get_card_number())
                self.deck_numbers.append(self.held_cards[0].get_card_number())
                self.held_cards[0].kill()
            elif effect[0] == "Defend" and character.is_enemy() == False:
                self.protagonist_sprite.set_defend()
                arcade.play_sound(self.defendSound)
                character.add_shield(effect[1])
                self.cards_played = self.cards_played + 1
                self.already_went = 1

                self.used_cards.append(self.held_cards[0].get_card_number())
                self.deck_numbers.append(self.held_cards[0].get_card_number())
                self.held_cards[0].kill()
            elif effect[0] == "Heal" and character.is_enemy() == False:
                self.protagonist_sprite.set_heal()
                arcade.play_sound(self.healSound)
                character.add_health(effect[1])
                self.cards_played = self.cards_played + 1
                self.already_went = 1

                self.used_cards.append(self.held_cards[0].get_card_number())
                self.deck_numbers.append(self.held_cards[0].get_card_number())
                self.held_cards[0].kill()
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
        self.cursor_list.draw()
        
        for character in self.character_list:
            character.next_image_idle()

        for card in self.deck:
            output = card.effect_string()
            arcade.draw_text(output, card.center_x - 20, card.center_y, arcade.color.BLACK, 14)
        # Put the text on the screen.
        for character in self.character_list:
            if character.is_character() == True:
                output = f"Health: {character.get_health()}\nShield: {character.get_shield()}"
                if character.is_enemy():
                    output = output + f"\nStrength: {character.get_strength()}"
                arcade.draw_text(output, character.center_x - 40, character.center_y + 125, arcade.color.WHITE, 14)
        if self.game_over == True:
            arcade.draw_text(f"  GAME OVER\nYour Score: {self.score}", SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT / 2 + 250, arcade.color.WHITE, 28)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the cursor sprite to match the mouse x, y

        self.cursor_sprite.center_x = x + 22
        self.cursor_sprite.center_y = y - 27
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.deck.update()
        self.character_list.update()
        self.cursor_list.update()
        number_of_enemies = 0
        

        for character in self.character_list:
            if character.is_enemy:
                number_of_enemies += 1
        if number_of_enemies == 1:
            self.score += 1
            new_enemies = self.score
            if new_enemies > 3:
                new_enemies = 3
            for i in range(0, new_enemies):
                if i == 1:
                    enemy_sprite = Enemy("z_images/Enemy.png", ENEMY_SPRITE_SCALING)
                    enemy_sprite.center_x = SCREEN_WIDTH - (390 * (i + 1))
                    enemy_sprite.center_y = 230
                    self.character_list.append(enemy_sprite)
                else:
                    enemy_sprite = Enemy("z_images/Enemy.png", ENEMY_SPRITE_SCALING)
                    enemy_sprite.center_x = SCREEN_WIDTH - (390 * (i + 1))
                    enemy_sprite.center_y = 250
                    self.character_list.append(enemy_sprite)

        # Generate a list of all sprites that collided with the player.
        cards_hit_list = arcade.check_for_collision_with_list(self.deck[0], self.deck)

        for character in self.character_list:
            if character.get_health() <= 0:
                character.set_dead()
            character.next_idle()

        if len(cards_hit_list) == len(self.deck) - 1:
            for card in cards_hit_list:
                card.center_x = 90
                card.center_y = SCREEN_HEIGHT - 70

        if self.protagonist_sprite.get_health() <= 0:
            self.game_over = True
        counter = 0
        for card in self.deck:
            counter += 1
        
        
        self.empty_slots = [1, 2, 3, 4, 5]
        slot_num = 0
        for i in self.empty_slots:
            match = False
            for card in self.deck:
                slot = card.get_slot()
                if i == slot:
                    match = True
            if match == False:
                self.empty_slots[slot_num] = 0
            slot_num += 1


        if counter <= 2:
            slot_num = 0 
            for j in self.empty_slots:
                slot_num += 1
                if j == 0:
                    card = Card("z_images/card1.png", 0.5, self.deck_numbers[0])
                    card.set_slot(slot_num)
                    self.deck.append(card)  
                    self.deck_numbers.pop(0)
                
                

        if self.cards_played % 3 == 0 and self.cards_played > 0 and self.already_went == 1:
            for character in self.character_list:
                if character.is_enemy():
                    character.reset_shield()
                    intent = character.get_intent()
                    if character.get_health() > 0:
                        if intent == "attack":
                            self.protagonist_sprite.do_damage(character.get_value())
                            character.set_attack()
                        elif intent == "defend":
                            character.add_shield(character.get_value())
                            character.set_defend()
                        elif intent == "heal":
                            character.add_health(character.get_value())
                            character.set_heal()
                        elif intent == "strengthen":
                            character.add_strength()
                            character.set_strengthen()
                self.already_went = self.already_went + 1
            
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