# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 09:33:00 2020

@author: eshah
"""

import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
digits = mnist.load_data()
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
np.set_printoptions(linewidth=90, formatter={'all': lambda x: '{0}'.format(x)})

for row in train_images[0]:
    print(row)
plt.imshow(train_images[1], cmap='binary')
plt.imshow(keras.utils.to_categorical(train_labels, 10)[:10], cmap='binary')