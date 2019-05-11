{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from colorfight import Colorfight\n",
    "from colorfight.user import User\n",
    "from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS\n",
    "\n",
    "class User2(User):\n",
    "    \n",
    "    def __init__(self):\n",
    "        User.__init__(self)\n",
    "        self.wells = 0\n",
    "        self.mines = 0\n",
    "        self.forts = 0\n",
    "        self.home = 1\n",
    "        self.homeLocation = Position()\n",
    "        self.tiles = len(cells)\n",
    "        self.tilesTaken = 0;\n",
    "    \n",
    "    def _update_building_info_(self.cells)    \n",
    "        for i, j in cells:\n",
    "            if j.is_home() == False:\n",
    "                if j.building == BLD_ENERGY_WELL:\n",
    "                    self.wells += 1\n",
    "                elif j.building == BLD_GOLD_MINE:\n",
    "                    self.mines += 1\n",
    "                elif j.building == BLD_FORTRESS:\n",
    "                    self.forts += 1\n",
    "            else\n",
    "                self.homeLocation = i.copy()\n",
    "\n",
    "    def _update_info(self, info):\n",
    "        for field in info:\n",
    "            if field != 'cells':\n",
    "                setattr(self, field, info[field])\n",
    "\n",
    "    def info(self):\n",
    "        return {\"uid\":self.uid, \\\n",
    "                \"username\": self.username, \\\n",
    "                \"energy\": self.energy, \\\n",
    "                \"gold\": self.gold, \\\n",
    "                \"dead\": self.dead, \\\n",
    "                \"energy_source\": self.energy_source, \\\n",
    "                \"gold_source\": self.gold_source, \\\n",
    "                \"cells\": [cell.position.info() for cell in self.cells.values()]}"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
