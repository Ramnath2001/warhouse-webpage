import os
from tabnanny import verbose
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np
import cv2
with tf.device("/CPU:0"):
    testimg = cv2.imread('D:/web_dev/warehouse-system/Images/camera_data.jpg')
    testimg = cv2.resize(testimg, (224, 224))
    testimg = np.expand_dims(testimg, axis = 0)
    # model = tf.keras.models.load_model('C:/Users/Ramnath/ML/finalModel2.h5')
    model = tf.keras.models.load_model('D:/web_dev/warehouse-system/python_scripts/keras_model.h5')
    result = model.predict(testimg/255, verbose=0)
    s = list(result[0])
    str_result = ' '.join([str(elem) for elem in s])
    index = np.argmax(result)
    final_result = ""
    if result[0][index] < 0.50:
        final_result = "cannot predict"
    elif index == 0:
        final_result = "Rats"
    elif index == 1:
        final_result = "Fire"
    else:
        final_result = "Human"

    api_res_data = [final_result, str_result]   
    print(api_res_data)
    # print(final_result)
    # print(s)
    
    