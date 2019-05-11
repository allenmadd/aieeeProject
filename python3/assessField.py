#
#values of making certain moves on certain tiles
#
#Uses data from user2
#creates a structure that contains the values of making moves on certain tiles without considering what other people would do 

def assessField():
	from colorfight import Colorfight
	import time
	import random
	from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS


	cellNames = ''
	cellAttackValue = () #[0] the gold that you can earn from it for the rest of the game. [1] the amount of energy you have to spend
	cellUpgradeValue = () #[0] the gold that you 
	attackDict =  {'Name' : 'Value'}
	upgradeDict = {'Name' : 'Value'}

	# Get all my cells.
	for cell in game.me.cells.values():

            #figure out your adjacent cells
            for pos in cell.position.get_surrounding_cardinals():
            	c = game.game_map[pos]
                # Get the MapCell object of that position
                #
                #attacking outcomes
                #

                if c.owner != game.uid:
             	    #attacking
					cellNames = str(cell.position.get_surrounding_cardinals(pos)) #name of the cell pos
					
					cellAttackValue[0] = gold *turn
					cellAttackValue[1] = c.attack_cost

					#update dictionary if its possible to even get this 
					if cellAttackValue[1] > me.energy:
						attackDict.update({cellNames: cellAttackValue})


      	 	#
        	#upgrading outcomes
        	#
        	if cell.building.can_upgrade and \
        	(cell.building.is_home or cell.building.level < me.tech_level) and \
        	cell.building.upgrade_gold < me.gold and \
        	cell.building.upgrade_energy < me.energy:

        		cellUpgradeValue[0] = 
















