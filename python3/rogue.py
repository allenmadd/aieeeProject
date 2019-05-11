#
#madeleine goes rogue
#
from colorfight import Colorfight
import time
import random
from colorfight.constants import BLD_GOLD_MINE, BLD_ENERGY_WELL, BLD_FORTRESS

import numpy as np
from io import BytesIO
from keras.layers import Input,BatchNormalization,Conv2D, Activation
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Model
from keras.utils.vis_utils import plot_model
from keras.optimizers import Adam
import os


# Create a Colorfight Instance. This will be the object that you interact
# with.
game = Colorfight()

# Connect to the server. This will connect to the public room. If you want to
# join other rooms, you need to change the argument
game.connect(room = 'public')

# game.register should return True if succeed.
# You need to set a password. For the example AI, the current time is used
# as the password. You should change it to something that will not change 
# between runs so you can continue the game if disconnected.
if game.register(username = 'Chlae', \
        password = 'charlesclaremadeleine'):

