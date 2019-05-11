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
import classify

def allocate(enemyClassifications, tileClassifications, selfBot, game):
    enemyClassifications = Classify()

    totWeight = sum(enemyClassifications.aggressive)

def move(enemyClassifications, tileClassifications, selfBot, game):