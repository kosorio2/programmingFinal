# MIND OF CARDS 
We are going to create a python game. The game will have a player and an enemy. The player will have a choice of attacks while the enemy will give a random attack. The attacks will determine the (health) of both, player and enemy, and the level of the game ends when either one of the two “health bars” hits zero. We are planning on starting with three levels (easy, medium, and hard).
More information coming...

## Getting Started
---
To start the game type the following commands:
  cd Cardsgame
  cd cards
  cd data
  python menumain.py 

  The menu will then  be displayed. Use the arrow keys on keyboard to select "Start game" and then press enter. The game should then run. 
  You control the game with the mouse. 


## Rules of the Game

The objective of the game is to destroy the enemy by using differemt cards.
There are three types of cards: Attack, Heal, and Defend. 
Each card works as follows
Attack: Takes 10 points from the enemy's health. It can only be used against the enemy.
Heal: Restores 5 points of the player's (your) health. It cannot be used on the enemy.
Defend: Gives the player an extra protection (10 points) from the enemy's attack. 

Each turn, the player can use three cards to either attack, heal, or defend himself against the enemy. The enemy then gets one turn
and randomly chooses fmro the same three options. 

The first one to get 0 points looses. 

Good Luck! May the odds be ever in your favor...

## Project Structure
---
The project files and folders are organized as follows:
```
root                    Cardsgame
+-- docs                (project documentation)
+-- cards              [src code files - rename for project] TBD... This will be rename after we decide the name of the game
  +-- data               (program data files)
                          init
                          background_sounds
                          character
                          card
                          cursor
                          director
                          enemy
                          menu
                          menuGamy
                          menumain
                          player   
    +-- z_images          (program asset files) Images,  backgrounds, sprite images..
    +-- sounds          all the sounds and music in the game.
+-- LICENSE             (license file) © 2021 All Rights Reserved.
+-- README.md           (general info) Game information, game instructions, and game general design.
```

## Required Technologies
---
Python 3
Python Libraries 
  random
  arcade
  NumPy
  Sys
  pygame


## Authors
---
mor17097@byui.edu
oso16001@byui.edu
bel8035@byui.edu