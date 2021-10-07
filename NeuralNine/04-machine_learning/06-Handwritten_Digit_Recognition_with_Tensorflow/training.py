import numpy as np
import tensorflow as tf 

# load data of real handwriting digits
mnist = tf.keras.datasets.mnist
# split into training data and test data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
# create a basic neural network
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# adding hidden two layers
# units is number on neurons
model.add(tf.keras.layers.Dense(units=300, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=200, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=100, activation=tf.nn.relu))
# output layers
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))
# =================
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train,y_train,epochs=5)

loss, accuracy = model.evaluate(x_test,y_test)
print(accuracy)
print(loss)
model.save('./04-machine_learning/06-Handwritten_Digit_Recognition_with_Tensorflow/model/digits')

