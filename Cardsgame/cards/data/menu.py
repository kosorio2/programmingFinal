import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.Instructionsx, self.Instructionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Luck of the Draw!', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Instructions", 20, self.Instructionsx, self.Instructionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.Instructionsx + self.offset, self.Instructionsy)
                self.state = 'Instructions'
            elif self.state == 'Instructions':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Instructions':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.Instructionsx + self.offset, self.Instructionsy)
                self.state = 'Instructions'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Instructions':
                self.game.curr_menu = self.game.Instructions
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class InstructionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Instructions'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            plusten=10
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Instructions', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("The objective of the game is to kill the enemy by either attacking or defending and healing yourself.", 9, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + plusten)
            self.game.draw_text("You are dealt 5 random cards. Each turn you can select three and wait for the opponent to", 9, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + plusten*2)
            self.game.draw_text("make a move. Attacking only works against the enemy, while healing and defending only work on", 9, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + plusten*3)
            self.game.draw_text("the player. Drag a card with your mouse and release it on your desired target", 9, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + plusten*4)
            self.game.draw_text("If you beat the 3 enemies, you win!", 9, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + plusten*5)
            self.game.draw_text("To begin, pick and enemy and a player and begin. Good Luck!", 9, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + plusten*6)
            self.game.draw_text("Press the backspace key to go back to the main menu.", 9, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + plusten*12)
            # Attacking only works agains the enemy, while healing and defending only works on the player. \n Drag the desire card with your mouse and 
            # release it on your desired target. Be careful with the enemy because he will strike back. As you kill enemies, you get more points and advance levels.
            # There are _____ levels and it ends after killing the most dangerous enemy. Good luck!""", 15, self.volx, self.voly)
            #self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('Jacob Morgan', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('Kathy Osorio', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 60)
            self.game.draw_text('Akemi Beltran', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 80)
            self.blit_screen()