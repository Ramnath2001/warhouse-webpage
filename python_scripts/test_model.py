import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

import tensorflow as tf


# Load the model
with tf.device("/CPU:0"):
    model = load_model('D:/web_dev/warehouse-system/python_scripts/keras_model.h5', compile=False)

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open('D:/web_dev/warehouse-system/Images/camera_data.jpg')
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference

    prediction = model.predict(data)
    s = list(prediction[0])
    str_result = ' '.join([str(elem) for elem in s])

    index = np.argmax(prediction)
    final_result = ""
    if prediction[0][index] < 0.50:
        final_result = "cannot predict"
    elif index == 0:
        final_result = "Fire"
    else:
        final_result = "Human"
    api_res_data = [final_result, str_result]   
    print(api_res_data)