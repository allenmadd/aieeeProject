#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from colorfight import Colorfight
from colorfight.user import User
from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS

class User2(User):
    
    def __init__(self):
        User.__init__(self)
        self.wells = 0
        self.mines = 0
        self.forts = 0
        self.home = 1
        self.homeLocation = Position()
        self.tiles = len(cells)
        self.tilesTaken = 0;
    
    def _update_building_info_(self.cells)    
        for i, j in cells:
            if j.is_home() == False:
                if j.building == BLD_ENERGY_WELL:
                    self.wells += 1
                elif j.building == BLD_GOLD_MINE:
                    self.mines += 1
                elif j.building == BLD_FORTRESS:
                    self.forts += 1
            else
                self.homeLocation = i.copy()

    def _update_info(self, info):
        for field in info:
            if field != 'cells':
                setattr(self, field, info[field])
        getTilesTaken(map1, map2)

    def info(self):
        return {"uid":self.uid,                 "username": self.username,                 "energy": self.energy,                 "gold": self.gold,                 "dead": self.dead,                 "energy_source": self.energy_source,                 "gold_source": self.gold_source,                 "cells": [cell.position.info() for cell in self.cells.values()]}
        
    

