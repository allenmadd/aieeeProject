
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
from move import move
import numpy as np
from classify import Classification

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
        users = game.users
        attackDict = assessField(game)[0]
        enemyClassifications = Classification(users,me.username)
        attackAlloc = .5*me.energy #allocate(enemyClassifications, attackDict, me, game, users)
        maxReward = 0
        best = 0
        while(best != -1):
            best = -1
            for i in attackDict:
                if(attackDict[i][0] - attackDict[i][1] > maxReward and attackAlloc > 100+attackDict[i][1]):
                    maxReward = attackDict[i][0] - attackDict[i][1]
                    best = i
            cmd_list.append(game.attack(i,attackDict[best][1]) + np.random.randint(0,100))
    




        # Send the command list to the server
        #
        #Identify Nearby Players/ Use their previous plays to classify them
        #
          #  classifyEnemies()

        #
        #Decide what to do based on how we classify them
        #
       # move()






