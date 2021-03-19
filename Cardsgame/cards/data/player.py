import random
import time
import sys

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Player():
    
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.wins = 0


    def calculate_damage(self, damage_amount, attacker):


        player = self.name
        enemy = attacker

    
        if (damage_amount > self.health):
            overkill = abs(self.health - damage_amount)
            points = overkill
            self.health = 0
            if (overkill > 0):
                print(f"{player} takes fatal damage from {enemy}, with {points} overkill!")
            else:
                print(f"{player} takes fatal damage from {enemy}!")
        else:
            self.health -= damage_amount
            print(f"{player} takes {damage_amount} damage from {enemy}!")

    def calculate_heal(self, heal_amount):
        if (heal_amount + self.health > 100):
            self.health = 100
            print(f"{self.name} heals back to full health!")
        else:
            self.health += heal_amount
            print(f"{self.name} heals for {heal_amount}!")


def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


def get_selection():
    valid_input = False
    while (valid_input is False):
        print()
        choice = input("Select an attack: ")
        if (parse_int(choice) is True):
            return int(choice)
        else:
            print("The input was invalid. Please try again.")


def get_enemy_selection(health):
    sleep_time = random.randrange(2, 5)
    print("....thinking....")
    time.sleep(sleep_time)

    if (health <= 35):
        # Have the enemy heal ~50% of its turns when <= 35
        result = random.randint(1, 6)
        if (result % 2 == 0):
            return 3
        else:
            return random.randint(1, 2)
    elif (health == 100):
        return random.randint(1, 2)
    else:
        return random.randint(1, 3)


def play_round(enemy, human):
    game_in_progress = True
    current_player = enemy

    while game_in_progress:
        # swap the current player each round
        if (current_player == enemy):
            current_player = human
        else:
            current_player = enemy

        print()
        print(
            f"You have {human.health} health remaining and the "
            f"Enemy has {enemy.health} health remaining.")
        print()

        if (current_player == human):
            print("Available attacks:")
            print("1) Electrocute - Causes moderate damage.")
            print("2) Wild Swing - high or low damage, "
                  "depending on your luck!")
            print("3) Nature's Kiss - Restores a moderate amount of health.")
            print("4) Atomic Buster - It can take down your enemy's health by 20 points or completely fail.")
            print("5) Spear Throw - Goes straight to your enemy's shoulder (Damage is 15) or land in your feet (Damage 5).")
            move = get_selection()
        else:
            move = get_enemy_selection(enemy.health)

        if (move == 1):
            damage = random.randrange(18, 25)
            if (current_player == human):
                enemy.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, enemy.name.capitalize())
        elif (move == 2):
            damage = random.randrange(10, 35)
            if (current_player == human):
                enemy.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, enemy.name.capitalize())
        elif (move == 3):
            heal = random.randrange(18, 25)
            current_player.calculate_heal(heal)
        elif (move == 4):
            damage = random.choice([0, 20])
            if (current_player == human):
                enemy.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, enemy.name.capitalize())
        elif (move == 5):
            damage = random.choice([5, 15])
            if damage == 15:
                if (current_player == human):
                    enemy.calculate_damage(damage, human.name.capitalize())
                else:
                    human.calculate_damage(damage, enemy.name.capitalize())
            else:
                if (current_player == human):
                    human.calculate_damage(damage, human.name.capitalize())
                else:
                    enemy.calculate_damage(damage, enemy.name.capitalize())
        else:
            print ("The input was not valid. Please select a choice again.")

        if (human.health == 0):
            delay_print("Sorry, you lose!")
            enemy.wins += 1
            game_in_progress = False

        if (enemy.health == 0):
            print("Congratulations, you beat the enemy!")
            human.wins += 1
            game_in_progress = False


def start_game():
    print("Welcome to the As-Yet-Unnamed turn-based battle game!")

    enemy = Player("Enemy")

    name = input("Please enter your name: ")
    human = Player(name)

    keep_playing = True

    while (keep_playing is True):
        print("Current Score:")
        print(f"You - {human.wins}")
        print(f"Enemy - {enemy.wins}")

        enemy.health = 100
        human.health = 100
        play_round(enemy, human)
        print()
        response = input("Play another round?(Y/N)")
        if (response.lower() == "n"):
            break

start_game()