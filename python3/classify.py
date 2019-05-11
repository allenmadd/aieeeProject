from colorfight import Colorfight
from colorfight.user import User
import time
import random
import numpy as np
from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS


def agression(users):
    x = np.array[users.tileChange/max(users.tileChange), users.tilesTaken/max(users.tilesTaken), users.tilesTakenTotalmax(users.tilesTakenTotalmax)]
    weights = np.ones(len(x))
    return np.sum(x*weights,axis = 0)

def goodness(users):
    x = np.array[users.netWorth/max(users.netWorth), len(users.cells)/max(len(users.cells))]
    weights = np.ones(len(x))
    return np.sum(x*weights,axis = 0)

def defense(users):
    x = np.array[users.energy/max(users.energy), users.stuff/max(users.stuff)]
    weights = np.ones(len(x))
    return np.sum(x*weights,axis = 0)

def riskOfAttack(users):
    x = np.array[users.com/max(users.com), users.nearest/max(users.nearest), users.energy/max(users.energy)]
    weights = np.ones(len(x))
    return np.sum(x*weights,axis = 0)

def benefitOfBlitz(users, me):
    x = np.array[users.gold/max(users.gold), users.energy/max(users.energy), users.nearest/max(users.nearest), users.homeLocation/max(users.homeLocation)]
    weights = np.ones(len(x))
    return np.sum(x*weights,axis = 0)