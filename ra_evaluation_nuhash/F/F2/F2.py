import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import os
import cv2
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras import layers
from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Dropout, BatchNormalization, Input
from keras.utils.np_utils import to_categorical
from keras.callbacks import EarlyStopping
from keras import regularizers
from keras.datasets import mnist
import numpy as np



(x_train, y_train), (x_test, y_test) = mnist.load_data()
# one hot encode target values
#set number of categories
num_category = 10
# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_category)
y_test = keras.utils.to_categorical(y_test, num_category)


#Normalization
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

#Print Shapes
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


# define inputs
inputA = layers.Input(shape=(28,28,1))

# the first branch operates on the first input
x = layers.Conv2D(32,(3,3), activation="relu")(inputA)

# the second branch opreates on the second input
y = layers.Conv2D(32,(3,3),activation="relu")(inputA)

# combine the output of the two branches
combine = layers.add([x,y])

#Added layer
z = layers.Conv2D(32,(3,3), activation="relu")(combine)
#z = layers.Flatten()(z)
#Classification Layer
z = layers.Dense(128, activation='relu')(z)
z = layers.Dense(10,activation='softmax')(z)

model = Model(inputs=inputA, outputs=z)
model.summary()


model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
#Model Training
history = model.fit(x_train, y_train, batch_size=128, epochs=30, validation_split=0.2)


#Evaluation
test_scores = model.evaluate(x_test, y_test, verbose=2)
print("Test loss:", test_scores[0])
print("Test accuracy:", test_scores[1])