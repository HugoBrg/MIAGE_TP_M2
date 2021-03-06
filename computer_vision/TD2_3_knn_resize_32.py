# Hugo BERANGER - M2 MIAGE IA

# using the knn algorithm and checking the 5 closest neighbours
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import os
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import glob
import cv2
import time
from sklearn.neighbors import NearestCentroid

#!wget --no-check-certificate -r 'http://www.i3s.unice.fr/~sanabria/files/dataset.zip' -O dataset.zip
#!unzip -qq dataset.zip -d /home/hugo/Documents/
#!ls /home/hugo/Documents/dataset

#!wget --no-check-certificate -r 'http://www.i3s.unice.fr/~sanabria/files/animals_dataset.zip' -O animals_dataset.zip
#!unzip -qq animals_dataset.zip -d /home/hugo/Documents/
#!ls /home/hugo/Documents/animals_dataset

dataset_path = "/home/hugo/Documents/dataset/"

#dataset_path = "/home/hugo/Documents/animals_dataset/"

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

# knn
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_image_flatten, y_train)

# checking the knn score, its actually pretty bad because we don't check enough neighbours given the size of the dataset
print(knn.score(X_test_image_flatten, y_test))

# checking which k value is the best to use, only went to 100 cause I have a bad machine, the curve should go back down after a while because k checking too many neighbours isn't efficient


def check_results_different_k(from_k, to_k, X_train, X_val):
    scores = []
    k_values = []
    for k in range(from_k, to_k):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        scores.append(knn.score(X_val, y_val))
        k_values.append(k)
    plt.plot(k_values, scores)
    plt.show()


start_time = time.time()
check_results_different_k(2, 20, X_train_image_flatten, X_val_image_flatten)
print("--- %s seconds ---" % (time.time() - start_time))

k_best_result = 100
knn = KNeighborsClassifier(n_neighbors=k_best_result)
knn.fit(X_train_image_flatten, y_train)
print(knn.score(X_test_image_flatten, y_test))

# nearest centroind
nc = NearestCentroid()
nc.fit(X_train_image_flatten, y_train)
nc.score(X_test_image_flatten, y_test)
