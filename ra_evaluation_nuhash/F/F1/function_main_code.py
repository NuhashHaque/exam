import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.layers import Input, Dense
from keras.models import Sequential


TEST_VALUES = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def format_input(i):
    return [1, i, i*i]


def generate_preprocess_data():
    values = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_train = np.array([5*i**2 + 7*i + 9 for i in values])
    x_train = np.array([format_input(i) for i in values])
    print(x_train.shape)
    print(y_train.shape)
    return x_train, y_train

def train_model(x_train, y_train):
    model = Sequential()
    model.add(Dense(50, input_shape=(3,), activation = 'relu'))
    model.add(Dense(25, activation = 'relu'))
    model.add(Dense(10, activation = 'relu'))
    model.add(Dense(1))

    model.compile(loss='mean_squared_error',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    model.fit(x_train, y_train, epochs=1000, batch_size=11)
    return model

def test_model(model):
    for i in TEST_VALUES:
        print('If we input to our model : ', i, ', Output is : ', round(model.predict([format_input(i)])[0][0]))
        
if __name__ == "__main__":
    x, y = generate_preprocess_data()
    model = train_model(x,y)
    test_model(model)



