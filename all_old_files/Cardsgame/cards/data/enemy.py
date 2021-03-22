import random
import time
import sys


class Enemy():
    """The responsibility of this class of objects is to have the enemy respond to players attack.
    
    Args:
        self (Enemy)
    """


    def __init__(self, enemy):
        self.enemy = enemy


    def calculate_damage(self, damage_amount, attacker): #calculates damage

        player = self.name
        enemy = attacker

        if (damage_amount > self.health):
            points = abs(self.health - damage_amount)
            self.health = 0
            if (points > 0):
                print(
                    f"{enemy} takes fatal damage from {player}, with {points} overkill!")  # You can put whatever the response is right here
            else:
                print(f"{player} takes fatal damage from {enemy}!")
        else:
            self.health -= damage_amount
            print(f"{enemy} takes {damage_amount} damage from {player}!")


    def calculate_heal(self, attacker, heal_amount): #caclulates how much healing the enemy will get

        enemy = attacker

        if (heal_amount + self.health > 100):
            enemy.health = 100
            print(f"{enemy} heals back to full health!")
        else:
            self.health += heal_amount
            print(f"{enemy} heals for {heal_amount}!")


    def get_selection(): #selects a random move for the enemy to use

        attacks = ['attack', 'heal', 'defense']
        choice = random.choice(attacks)
        print(choice)


    def get_enemy_selection(health): #Gives the enemy options to attack, defend, or heal, according to its health condition.  
        sleep_time = random.randrange(2, 5)
        time.sleep(sleep_time)

        if (health <= 35):
            # Have the enemy heal ~50% of its turns when <= 35
            result = random.randint(1, 3) 
            if (result % 2 == 0):
                return 3
            else:
                return random.randint(1, 2)
        elif (health == 100):
            return random.randint(1, 2)
        else:
            return random.randint(1, 6)


    def enemy_move(self): #Assigns the enemy a value for each move
        game_in_progress = True
        current_player = self.enemy

        while game_in_progress:
            if (current_player == self.enemy):

                move = self.get_selection(self.enemy.health)

                if (move == 'attack'):
                    damage = random.randrange(18, 25)
                    self.enemy.calculate_damage(damage)
                elif (move == 'defense'):
                    damage = 0
                    self.enemy.calculate_damage(damage)
                elif (move == 'heal'):
                    heal = random.randrange(18, 25)
                    current_player.calculate_heal(heal)
                    if (self.enemy.health < 20):
                        move == 'special attack'
                        damage = random.randrange(20, 50)
                        self.enemy.calculate_damage(damage)



