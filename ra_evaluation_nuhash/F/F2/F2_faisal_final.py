import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import layers



def create_data():
    """Generate Dataset

    Returns:
        tensors : train and test set 
    """
    X_train = np.random.rand(100,32, 32, 3)
    y_train = np.random.rand(100,28, 28, 32)
    X_test = np.random.rand(100,32, 32, 3)
    y_test = np.random.rand(100,28, 28, 32)

    return X_train, y_train, X_test, y_test

def create_model():
    """Model Architechture Build

    Returns:
        Keras Model: Model 
    """

    inputs1=keras.layers.Input(shape=(32,32,3))
    x=keras.layers.Conv2D(32,3,activation='relu')(inputs1)
    x=keras.layers.Activation('relu')(x)


    inputs2=keras.layers.Input(shape=(32,32,3))
    y=keras.layers.Conv2D(32,3,activation='relu')(inputs2)
    y=keras.layers.Activation('relu')(y)

    # add x and y 
    z=keras.layers.Add()([x,y])
    z=keras.layers.Conv2D(32,3)(z)
    z=keras.layers.Activation('relu')(z)
    
    model=keras.Model(inputs=[inputs1,inputs2],outputs=z)
    model.summary()
    model.compile(optimizer='adam',loss='mse')

    return model




if __name__ == "__main__":


    X_train, y_train, X_test, y_test = create_data()

    model = create_model()

    history=model.fit([X_train,X_train],y_train,epochs=10)

    results=model.evaluate([X_test,X_test],y_test)
    
    print(results)
