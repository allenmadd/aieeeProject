#
#Classifying enemies
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














