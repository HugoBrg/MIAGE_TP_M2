#!wget --no-check-certificate -r 'http://www.i3s.unice.fr/~sanabria/files/dataset.zip' -O dataset.zip
#!unzip -qq dataset.zip
#!ls dataset

import numpy as np
from keras.datasets import mnist
from sklearn.model_selection import train_test_split
import keras.utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import os
import glob
import cv2
from sklearn import preprocessing

#!wget --no-check-certificate -r 'http://www.i3s.unice.fr/~sanabria/files/dataset.zip' -O dataset.zip
#!unzip -qq dataset.zip -d /home/hugo/Documents/
#!ls /home/hugo/Documents/dataset

dataset_path = "/home/hugo/Documents/dataset/"

classes = os.listdir(dataset_path)

# array of images
X = []
for class_name in classes:
    class_path = dataset_path + class_name
    for image_path in glob.glob(class_path + "/*.jpg"):
        X.append(image_path)

# array of labels
y = []
for image_path in X:
    y.append(image_path.split('/')[-2])

# transform images name and labels into 0 and 1
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)

print(len(X))
print(len(y))
# split the dataset in 3 group : train, test and validation
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y)
X_test, X_val, y_test, y_val = train_test_split(
    X_test, y_test, test_size=0.5, stratify=y_test)

# resize the images in order to make the task easier for the algorithm


def read_images(X):
    X_image = []
    for image_path in X:
        image = cv2.imread(image_path)
        image_resize = cv2.resize(image, (32, 32))
        X_image.append(image_resize)
    return np.asarray(X_image)


# resizing
X_train_image = read_images(X_train)
X_test_image = read_images(X_test)
X_val_image = read_images(X_val)

# flatten the image because can means can only use vectors
X_train_image_flatten = X_train_image.reshape(
    X_train_image.shape[0], X_train_image.shape[1] * X_train_image.shape[2] * X_train_image.shape[3])
X_test_image_flatten = X_test_image.reshape(X_test_image.shape[0], -1)
X_val_image_flatten = X_val_image.reshape(X_val_image.shape[0], -1)

# ... and normalize the data (grey levels are integers from 0 to 255)
X_train_image_flatten = X_train_image_flatten.astype('float32')/255
X_test_image_flatten = X_test_image_flatten.astype('float32')/255
X_val_image_flatten = X_val_image_flatten.astype('float32')/255

print(X_train_image.shape[1] * X_train_image.shape[2] * X_train_image.shape[3])

# Let's build a simple neural network using the keras sequential method
model = Sequential()

model.add(Dense(1, input_dim=3072, activation='relu'))  # Using only one neuron

# softmax for the output using as many neurons as classes (10 in this case)
nb_classes = 2
model.add(Dense(nb_classes, activation='softmax'))
model.summary()  # This line is used to print the architecture of the model

model.compile(optimizer='sgd', loss='categorical_crossentropy',
              metrics=['accuracy'])

nb_neurons_first_layer = 16  # A completer
nb_neurons_second_layer = 16  # A completer
model = Sequential()

model.add(Dense(nb_neurons_first_layer, input_dim=3072, activation='relu'))
model.add(Dense(nb_neurons_second_layer, activation='relu'))

model.add(Dense(nb_classes, activation='softmax'))

model.compile(optimizer='sgd', loss='categorical_crossentropy',
              metrics=['accuracy'])

ourCallback = keras.callbacks.EarlyStopping(monitor='val_accuracy', min_delta=0.0001, patience=20)
print("Training....")
history = model.fit(X_train_image_flatten, y_train, validation_data=(
    X_val_image_flatten, y_val), epochs=300, batch_size=128, callbacks=[ourCallback])

# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()
