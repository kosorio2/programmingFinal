import time 
import numpy as np
import sys
import random 

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Actor:
    def __init__(self, name, types, moves, health='==================='):
        # save variables as attributes
        self.types = types
        self.name = name
        self.get_move_value = moves
        self.health = health
        self.bars = 20 # Amount of health bars


    def get_move_value(self, random_move):
        moves = {'Fire Ball' : 2, 
                'Sword Attack' : 4,
                'Double Strike' : 3, 
                'Face Punch': 5,
                'Defense': 3}

        list_conversion = list(moves.items())
            
  
        random_move = random.choice(list_conversion)

        return(random_move[1])



    def fight(self, movi):
        # Allow two Actor to fight each other

        player_movi = self.random_move

        enemy_movi = self.random_move

        while player_movi > enemy_movi:
            print("Player wins")
        while player_movi < enemy_movi:
            print("Enemy Wins")
        while player_movi == enemy_movi:
            print("Its a tie")




if __name__ == "new.py":

    enemy1 = Actor('Blade Vonner', 'Enemy1', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'])

    player = Actor('Player', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'])

    player.fight(enemy1)


 
        # # Print fight information
        # print("----Welcome to the Battle----")
        # print(f"\n{Player.name} VS {Enemy.name}")

        # time.sleep(2)


        # version = ['Player', 'Enemy1']
        # for i,k in enumerate(version):
        #         # Enemy is STRONG
        #         if Enemy.types == k:
        #             Enemy.moves *= 2
        #             Enemy.defense *= 2
        #             Player.attack /= 2
        #             Player.defense /= 2
        #             string_1_attack = '\nIts not very effective Player...'
        #             string_2_attack = '\nIts super effective Enemy!'

        #         # Enemy is WEAK
        #         if Enemy.types == version[(i+1)%2]:
        #             Player.attack *= 2
        #             Player.defense *= 2
        #             Enemy.attack /= 2
        #             Enemy.defense /= 2
        #             string_1_attack = '\nIts super effective Player!'
        #             string_2_attack = '\nIts not very effective Enemy...'
           