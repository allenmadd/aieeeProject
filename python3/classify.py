from colorfight import Colorfight
from colorfight.user import User
import time
import random
import numpy as np
from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS


class Classification:
    def __init__(self, users, username):
        self.aggression = self._Aggression(users)
        self.goodness = self._Goodness(users)
        self.defense = self._Defense(users)
        self.riskOfAttack = self._RiskOfAttack(users)
        self.benefitOfBlitz = self._BenefitOfBlitz(users, username)

    def _Aggression(self,users):
        x = np.array[users.tileChange/max(users.tileChange), users.tilesTaken/max(users.tilesTaken), users.tilesTakenTotalmax(users.tilesTakenTotalmax)]
        weights = np.ones(len(x))
        return np.sum(x*weights,axis = 0)

    def _Goodness(self,users):
        x = np.array[users.netWorth/max(users.netWorth), len(users.cells)/max(len(users.cells))]
        weights = np.ones(len(x))
        return np.sum(x*weights,axis = 0)

    def _Defense(self,users):
        x = np.array[users.energy/max(users.energy), users.forts/max(users.forts)]
        weights = np.ones(len(x))
        return np.sum(x*weights,axis = 0)

    def _RiskOfAttack(self,users):
        x = np.array[users.com/max(users.com), users.nearest/max(users.nearest), users.energy/max(users.energy)]
        weights = np.ones(len(x))
        return np.sum(x*weights,axis = 0)

    def _BenefitOfBlitz(self, users, username):
        x = np.array[users.gold/max(users.gold), users.energy/max(users.energy), users.nearest/max(users.nearest), users.homeLocation/max(users.homeLocation)]
        weights = np.ones(len(x))
        return np.sum(x*weights,axis = 0)


