from colorfight import Colorfight
from colorfight.user import User
#from colorfight.Position import Position
from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS

class User2(User):
    
    def __init__(self,last,lastUser):
        User.__init__(self)
        self.wells = 0
        self.mines = 0
        self.forts = 0
        self.home = 1
        self.homeLocation = 0
        self.tiles = len(self.cells)
        self.tilesTaken = 0
        self.tilesTakenTotal = 0
        self.tileChange = 0
        self._update_building_info_(last, lastUser)
    
    def _update_building_info_(self, last, lastUser = 0):    # last should be game map
        cells = self.cells
        for i, j in cells:
            if j.is_home() == False:
                if j.building == BLD_ENERGY_WELL:
                    self.wells += 1
                elif j.building == BLD_GOLD_MINE:
                    self.mines += 1
                elif j.building == BLD_FORTRESS:
                    self.forts += 1
            else:
                self.homeLocation = i.copy()
            if(lastUser == 0):
                return
            if(last[i].owner != j.owner):
                tilesTaken += 1
        self.tileChange = self.tiles - lastUser.tiles
        self.tilesTakenTotal = lastUser.tilesTakenTotal + tilesTaken
        
    

