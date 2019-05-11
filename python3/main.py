
#
#Colorfight AI created by the 3 stooges
# 11 May 2019
#

from colorfight import Colorfight
import time
import random
from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS
from assessField import assessField
from User2 import User2
#DONT FORGET TO IMPORT THINGS

# Create a Colorfight Instance.
global game
game = Colorfight()

# Connect to the server. This will connect to the public room.
game.connect(room = 'public2')

# game.register should return True if succeed.
if game.register(username = 'Chlane', \
                 password = 'charlesclaremadeleine'):

    # This is the game loop
    while True:
        # The command list we will send to the server
        cmd_list = []
        # The list of cells that we want to attack
        my_attack_list = []

        # Check if you exist in the game. If not, wait for the next round.
        me = game.me

        if game.me == None:
            continue
        game.update_turn()

        #make a move
        move() #CHARLES PUT THE CORRECT INPUTS HERE IF THEY ARE NEEDED AND SET TO THE CORRECT OUTPUTS IF NEEDED












        # Send the command list to the server
        #
        #Identify Nearby Players/ Use their previous plays to classify them
        #
          #  classifyEnemies()

        #
        #Decide what to do based on how we classify them
        #
       # move()






