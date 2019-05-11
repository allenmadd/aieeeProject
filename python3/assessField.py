#
#returns possible attacks and upgrades with costs
#

def assessField(game):
    from colorfight import Colorfight
    import time
    import random
    from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS


    cellNames = ''
    cellAttackValue = () #[0] the gold that you can earn from it for the rest of the game. [1] the amount of energy you have to spend
    cellUpgradeValue = () #[0] the gold that you spend to upgrade [1] the energy you spend to upgrade (not actually used in this format)

    attackDict =  {'Name' : 'Value'}
    upgradeDict = {'Name' : 'Value'}

    # Get all my cells.
    for cell in game.me.cells.values():
        for pos in cell.position.get_surrounding_cardinals():
            c = game.game_map[pos]
            if c.owner != game.uid:
#attacking
                cellNames = str(cell.position.get_surrounding_cardinals(pos)) #name of the cell pos
                cellAttackValue[0] = gold * (500-turn)
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
            upgradeDict.update({cellNames : (cell.building.upgrade_gold, cell.building.upgrade_energy)})

    return attackDict, upgradeDict
