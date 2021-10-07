import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Activation
from tensorflow.keras.optimizers import RMSprop
import os


filepath = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(filepath,'rb').read().decode(encoding='utf-8').lower()

text = text[300000:800000]
# take all the characters in 'text' and sort them
characters = sorted(set(text))
# make a dictionary with those caracters and its index
char_to_index = dict((c,i) for i, c in enumerate(characters))
index_to_char = dict((i,c) for i, c in enumerate(characters))

SEQ_LENGTH = 40
STEP_SIZE = 3

sentences = []
next_characters = []

for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i: i + SEQ_LENGTH])
    next_characters.append(text[i+SEQ_LENGTH])

x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype=np.bool)
y = np.zeros((len(sentences), len(characters)), dtype=np.bool)

for i, sentence in enumerate(sentences):
    for t, character in enumerate(sentence):
        x[i,t,char_to_index[character]] = 1
    y[i,char_to_index[next_characters[i]]] = 1

# Training
model = Sequential()
# adding the input layer, LSTM as a memory, it will remember the importan characters
model.add(LSTM(128, input_shape=(SEQ_LENGTH, len(characters))))
# hidden layer
model.add(Dense(len(characters)))
# otput layer
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer=RMSprop(learning_rate=0.01))
model.fit(x,y,batch_size=256, epochs=4)
# saving the model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR,'my_model')
model.save(model_path)