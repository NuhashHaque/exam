from statistics import mode
from tensorflow import keras
from keras.models import load_model

import numpy as np
import cv2
import matplotlib.pyplot as plt
 

def load_best_model():
    
    # load model
    model = load_model("C:/Users/Nuhash/Desktop/NSL_Exam/Solves/Part_B/Model/best_model.h5")
    # load single data
    return model


def inference(image_path,model):

    img = cv2.imread(image_path, 0)
    plt.imshow(img)
    plt.show()
    reshaped_img = img.reshape(1,784)
    predicted_img = model.predict(reshaped_img)
    output = predicted_img.reshape(28, 28)
    plt.imshow(output)
    plt.show()
    plt.imsave("./Inference_Image/sample_output/output.jpg", output)




if __name__ == "__main__":


    model = load_best_model()
    model.summary()
    #inferene image path
    path = "./Inference_Image/sample_input/337.jpg"
    inference(path,model)

