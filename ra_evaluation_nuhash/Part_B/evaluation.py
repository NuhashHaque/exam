from statistics import mode
from tensorflow import keras
from keras.models import load_model
from skimage.metrics import structural_similarity as ssim
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

from utils import *
from inference import *

def similarity_check(im_1, im_2):

    similarity = ssim(im_1, im_2)
    if similarity > 0.8:
        ans = 1
    else:
        ans = 0
    return ans







if __name__ == "__main__":

    generate_font_image()

    x, y = create_minst_dataset()

    syn_img_list = load_images_from_folder("./DataSet/Synthetic_Image")

    syn_img = generate_synthetic_image_dataset(y, syn_img_list)


    #visualize(10, x)
    #visualize(10, syn_img)

    x_train, y_train, x_val, y_val, x_test, y_test = normalize_split_data(x, syn_img)
    print(x_train.shape, y_train.shape, x_val.shape, y_val.shape, x_test.shape, y_test.shape)



    model = load_best_model()
    model.summary()



    decoded_imgs_train = model.predict(x_train)
    decoded_imgs_val = model.predict(x_val)
    decoded_imgs_test = model.predict(x_test)



    print(mean_squared_error(y_train, decoded_imgs_train))
    print(mean_squared_error(y_test, decoded_imgs_test))
    print(mean_squared_error(y_val, decoded_imgs_val))



    predicted_similarity_list_train = [similarity_check(y_train[i], decoded_imgs_train[i]) for i in range(x_train.shape[0])]
    actual_similarity_list_train = [1 for i in range(x_train.shape[0])]
    print("Training Accuracy: ")
    print(accuracy_score(actual_similarity_list_train, predicted_similarity_list_train))
    print(classification_report(actual_similarity_list_train, predicted_similarity_list_train))


    predicted_similarity_list_test = [similarity_check(y_test[i], decoded_imgs_test[i]) for i in range(x_test.shape[0])]
    actual_similarity_list_test = [1 for i in range(x_test.shape[0])]
    print("Testing Accuracy: ")
    print(accuracy_score(actual_similarity_list_test, predicted_similarity_list_test))
    print(classification_report(actual_similarity_list_test, predicted_similarity_list_test))



    predicted_similarity_list_val = [similarity_check(y_val[i], decoded_imgs_val[i]) for i in range(x_val.shape[0])]
    actual_similarity_list_val = [1 for i in range(x_val.shape[0])]
    print("Validation Accuracy: ")
    print(accuracy_score(actual_similarity_list_test, predicted_similarity_list_test))
    print(classification_report(actual_similarity_list_val, predicted_similarity_list_val))
    


