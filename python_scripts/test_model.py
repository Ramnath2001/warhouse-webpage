import os
from tabnanny import verbose
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import numpy as np
import cv2
with tf.device("/CPU:0"):
    testimg = cv2.imread('C:/Users/Ramnath/ML/rat1.jpg')
    testimg = cv2.resize(testimg, (128, 128))
    testimg = np.expand_dims(testimg, axis = 0)
    model = tf.keras.models.load_model('C:/Users/Ramnath/ML/finalModel3.h5')
    result = model.predict(testimg/255, verbose=0)
    print(result)