import pyrebase
import os
config = {
    'apiKey': "AIzaSyDH3n5SqSt1hGX48joRk1CqyP9OdbW79Xs",
    'authDomain': "warehouse-7b5d5.firebaseapp.com",
    'databaseURL': "https://warehouse-7b5d5-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "warehouse-7b5d5",
    'storageBucket': "warehouse-7b5d5.appspot.com",
    'messagingSenderId': "17994702707",
    'appId': "1:17994702707:web:3d5df1e44366aa34106f06",
    'measurementId': "G-361103K28G"
}


firebase = pyrebase.initialize_app(config)
db = firebase.storage()
db.child("camera_data.jpg").download(filename="D:/web_dev/warehouse-system/Images/camera_data.jpg")