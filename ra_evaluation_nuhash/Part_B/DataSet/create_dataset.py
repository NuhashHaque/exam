import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import os
import cv2
from tensorflow import keras
from keras.datasets import mnist


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def generate_font_image():
    for i in range(10):
        img = Image.new('RGB', (28,28), (0,0,0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("./DataSet/Font/times-roman.ttf", 30)
        draw.text((6, -1),str(i),(255,255,255),font=font)
        #resized_img = img.resize((round(28), round(28)))
        thresh = 200
        fn = lambda x : 255 if x > thresh else 0
        img = img.convert('L').point(fn, mode='1')
        img.save('./DataSet/Synthetic_Image/digit_number_img_'+str(i)+'.jpg')

def load_images_from_folder(folder):

    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),0)
        if img is not None:
            images.append(img)
    return images



def visualize(n, image_array):
    # How many digits we will display
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # Display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(image_array[int(i)].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()




def create_minst_dataset():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    #print(x_train.shape)
    x = np.concatenate((x_train,x_test), axis= 0)
    #print(x.shape)
    y = np.concatenate((y_train, y_test), axis = 0)
    #y = np.reshape(y,(-1,1))
    #print(y.shape)
    return x, y

def generate_synthetic_image_dataset(label_list , syn_image_list):

    syn_img_list = []
    for i in label_list:
        syn_img_list.append(syn_image_list[i])

    syn_img_numpy =  np.array(syn_img_list)
    return syn_img_numpy



if __name__ == "__main__":
    
    generate_font_image()

    x, y = create_minst_dataset()

    syn_img_list = load_images_from_folder("C:/Users/Nuhash/Desktop/NSL_Exam/Solves/Part_B/DataSet/Synthetic_Image")

    syn_img = generate_synthetic_image_dataset(y, syn_img_list)

    #print(syn_img.shape)
    visualize(10, x)
    visualize(10, syn_img)




