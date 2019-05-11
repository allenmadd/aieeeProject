#
#Colorfight AI created by the 3 stooges
# 11 May 2019
#

from colorfight import Colorfight
import time
import random
from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS
import assessField
#DONT FORGET TO IMPORT THINGS



# Create a Colorfight Instance. This will be the object that you interact
# with.
game = Colorfight()

# Connect to the server. This will connect to the public room. If you want to
# join other rooms, you need to change the argument
game.connect(room = 'public')

# game.register should return True if succeed.
# You need to set a password. For the example AI, the current time is used
# as the password. You should change it to something that will not change 
# between runs so you can continue the game if disconnected.
if game.register(username = 'Chlane', \
        password = 'charlesclaremadeleine'):
    # This is the game loop
    while True:

        #
        #Assess where we are 
        #Input: nothing
        #output: the taxes, cost/benefit of stuff
        #
        

        #
        #evaluate the value of the titles
        #
        attackDict, upgradeDict = assessField()

        maxReward = 0
        bestAttack= ''
        
        for x in attackDict.values():
            if x[0]-x[1] > maxReward:
                maxReward = x[0]-x[1]
                bestAttack=attackDict(x)




        #
        #Identify Nearby Players/ Use their previous plays to classify them
        #
        classifyEnemies()

        #
        #Decide what to do based on how we classify them
        #
        move()






