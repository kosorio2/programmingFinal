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
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.types = types
        self.name = name
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars


    def fight(Player, Enemy):
        # Allow two Actor to fight each other

        # Print fight information
        print("---- ActorE BATTLE-----")
        print(f"\n{Player.name}") #Player. (Whenever you see Player. is )
        print("TYPE/", Player.types)
        print("ATTACK/", Player.attack)
        print("DEFENSE/", Player.defense)
        print("LVL/", 3*(1+np.mean([Player.attack,Player.defense])))
        print("\nVS")
        print(f"\n{Enemy.name}") #Enemy 
        print("TYPE/", Enemy.types)
        print("ATTACK/", Enemy.attack)
        print("DEFENSE/", Enemy.defense)
        print("LVL/", 3*(1+np.mean([Enemy.attack,Enemy.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if Player.types == k:
                # Both are same type
                if Enemy.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Enemy is STRONG
                if Enemy.types == version[(i+1)%3]:
                    Enemy.attack *= 2
                    Enemy.defense *= 2
                    Player.attack /= 2
                    Player.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Enemy is WEAK
                if Enemy.types == version[(i+2)%3]:
                    Player.attack *= 2
                    Player.defense *= 2
                    Enemy.attack /= 2
                    Enemy.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


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
    enemy1 = Actor('Enemy', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK': 4, 'DEFENSE': 2})
    enemy2 = Actor('Enemy', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 5, 'DEFENSE':10})
    enemy3 = Actor('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})

    player = Actor('Player', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    


    player.fight(enemy2) # Get them to fight