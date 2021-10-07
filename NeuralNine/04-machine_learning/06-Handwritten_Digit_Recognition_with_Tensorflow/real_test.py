import numpy as np
import matplotlib.pyplot as pt
import cv2 as cv
import tensorflow as tf 
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(BASE_DIR, "data_test")

# load model saved
model = tf.keras.models.load_model('./04-machine_learning/06-Handwritten_Digit_Recognition_with_Tensorflow/model/digits')
model.summary()

for root, dirs, files in os.walk(img_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            img = cv.imread(path)[:,:,0]
            img = np.invert(np.array([img]))
            prediction = model.predict(img)
            print(f"The result may be: {np.argmax(prediction)}")
            pt.imshow(img[0], cmap=pt.cm.binary)
            pt.show()

    
