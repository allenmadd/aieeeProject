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
    
        


def move(selfBot, game):
    attackDict = assessField(game)[0]
    enemyClassifications = Classification(users,selfBot.username)
    if(enemyClassifications.riskOfAttack > 1):
        Defend
    elif((enemyClassifications.benefitOfBlitz -enemyClassifications.goodness) > 1):
        maxReward = 0
        best = -1
        for i in attackDict.keys:
            if(attackDict[i][0] - attackDict[i][1]) > maxReward:
                maxReward = attackDict[i][0] - attackDict[i][1]
                best = i