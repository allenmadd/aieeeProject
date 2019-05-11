#
#
#move
#our main model
#

from colorfight import Colorfight
from colorfight.user import User
import time
import random
import numpy as np
from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS
from classify import Classification
from assessField import assessField

def allocate(enemyClassifications, tileClassifications, selfBot, game, users):
    #determine resources to allocate to certain moves
    return .5*game.me.energy
    


def move(game):
    selfBot = game.me
    users = game.users
    attackDict = assessField(game)[0]
    enemyClassifications = Classification(users,selfBot.username)
    attackAlloc = allocate(enemyClassifications, attackDict, selfBot, game, users)
    maxReward = 0
    best = 0
    while(best != -1):
        best = -1
        for i in attackDict:
            if(attackDict[i][0] - attackDict[i][1] > maxReward and attackAlloc > 100+attackDict[i][1]):
                maxReward = attackDict[i][0] - attackDict[i][1]
                best = i
        cmd_list.append(game.attack(i,attackDict[best][1]) + np.random.randint(0,100))
    