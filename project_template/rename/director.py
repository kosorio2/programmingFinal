import time
import numpy as np
import sys
import random

# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class Actor:
    def __init__(self, name, types, moves, attack, defense, health='==================='):
        # save variables as attributes
        self.types = types
        self.name = name
        self.moves = moves
        self.attack = attack['ATTACK']
        self.defense = defense['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars


    def fight(Player, Enemy):
        # Allow two Actor to fight each other

        # Print fight information
        print("----Welcome to the Battle----")
        print(f"\n{Player.name} VS {Enemy.name}") #Player. (Whenever you see Player. is )

        time.sleep(2)

        # Consider type advantages
        version = ['Player', 'Enemy1']
        for i,k in enumerate(version):
                # Enemy is STRONG
                if Enemy.types == k:
                    Enemy.attack *= 2
                    Enemy.defense *= 2
                    Player.attack /= 2
                    Player.defense /= 2
                    string_1_attack = '\nIts not very effective Player...'
                    string_2_attack = '\nIts super effective Enemy!'

                # Enemy is WEAK
                if Enemy.types == version[(i+1)%2]:
                    Player.attack *= 2
                    Player.defense *= 2
                    Enemy.attack /= 2
                    Enemy.defense /= 2
                    string_1_attack = '\nIts super effective Player!'
                    string_2_attack = '\nIts not very effective Enemy...'


        # Now for the actual fighting...
        # Continue while Actor still have health
        while (Player.bars > 0) and (Enemy.bars > 0):
            # Print the health of each Actor
            print(f"\n{Player.name}\t\tHLTH\t{Player.health}")
            print(f"{Enemy.name}\t\tHLTH\t{Enemy.health}\n")

            print(f"Go {Player.name}!")
            for i, x in enumerate(Player.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Player.name} used {Player.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Enemy.bars -= Player.attack
            Enemy.health = ""

            # Add back bars plus defense boost
            for j in range(int(Enemy.bars+.1*Enemy.defense)):
                Enemy.health += "="

            time.sleep(1)
            print(f"\n{Player.name}\t\tHLTH\t{Player.health}")
            print(f"{Enemy.name}\t\tHLTH\t{Enemy.health}\n")
            time.sleep(.5)

            # Check to see if Actor fainted
            if Enemy.bars <= 0:
                delay_print("\n..." + Enemy.name + ' fainted.')
                break

            # Enemys turn

            print(f"Go {Enemy.name}!")
            for i, x in enumerate(Enemy.moves):
                print(f"{i+1}.", x)
            index = random.randint(1, 4)
            delay_print(f"\n{Enemy.name} used {Enemy.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            Player.bars -= Enemy.attack
            Player.health = ""

            # Add back bars plus defense boost
            for j in range(int(Player.bars+.1*Player.defense)):
                Player.health += "="

            time.sleep(1)
            print(f"{Player.name}\t\tHLTH\t{Player.health}")
            print(f"{Enemy.name}\t\tHLTH\t{Enemy.health}\n")
            time.sleep(.5)

            # Check to see if Actor fainted
            if Player.bars <= 0:
                delay_print("\n..." + Player.name + ' fainted.')
                break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.\n")






if __name__ == '__main__':
    #Create Actor
 
    enemy1 = Actor('Blade Vonner', 'Enemy1', ['Fire Ball', 'Sword Attack', 'Double Strike', 'Face Punch'], {'ATTACK':2})
    enemy3 = Actor('Thorne Thornheart', 'Enemy1', ['Fire Ball', 'Sword Attack', 'Double Strike', 'Face Punch'],{'ATTACK':2})

    player = Actor('Kim', 'Player', ['Fire Ball', 'Sword Attack', 'Double Strike', 'Face Punch'],{'ATTACK':2, 'DEFENSE':2})
    


    player.fight(enemy1) # Get them to fight