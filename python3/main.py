
#
#Colorfight AI created by the 3 stooges
# 11 May 2019
#

from colorfight import Colorfight
import time
import random
from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS
from assessField import assessField
#DONT FORGET TO IMPORT THINGS



# Create a Colorfight Instance. This will be the object that you interact
# with.

global game
game = Colorfight()

# Connect to the server. This will connect to the public room. If you want to
# join other rooms, you need to change the argument
game.connect(room = 'public4')

# game.register should return True if succeed.
# You need to set a password. For the example AI, the current time is used
# as the password. You should change it to something that will not change
# between runs so you can continue the game if disconnected.
if game.register(username = 'Chlane', \
                 password = 'charlesclaremadeleine'):

    game.update_turn()

    # Check if you exist in the game. If not, wait for the next round.
    # You may not appear immediately after you join. But you should be
    # in the game after one round.

    me = game.me
    # This is the game loop
    while True:
        if game.me == None:
            continue
        #
        #evaluate the value of the titles
        #
        # The command list we will send to the server
        cmd_list = []
        # The list of cells that we want to attack
        my_attack_list = []

        attackDict, upgradeDict = assessField(game)
        maxReward = 0
        bestAttack= ''

        for x in attackDict.values():
            if x[0]-x[1] > maxReward:
                maxReward = x[0]-x[1]
                bestAttack=attackDict(x)
        #just adding this for demonstrative purposes
        cmd_list.append(game.attack(bestAttack, x[1]))
        print(f"We are attacking ({pos.x}, {pos.y}) with {c.attack_cost} energy")
        game.me.energy -= c.attack_cost
        my_attack_list.append(c.position)


        # Send the command list to the server
        result = game.send_cmd(cmd_list)
        print(result)

        #
        #Identify Nearby Players/ Use their previous plays to classify them
        #
      #  classifyEnemies()

        #
        #Decide what to do based on how we classify them
        #
       # move()






