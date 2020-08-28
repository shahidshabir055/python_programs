# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:53:48 2020

@author: eshah
"""

import os,cv2
import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
from sklearn.cross_vaidation import train_set_split

from keras import backend as K
K.set_image_dim_ordering('tf')

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout,Activation, Flatten
from keras.layers.convolutional import Convolution2D,MaxPolling2D
from keras.optimizers import SGD,RMSprop,adam

img_rows=128
img_cols=128
num_channel=1
