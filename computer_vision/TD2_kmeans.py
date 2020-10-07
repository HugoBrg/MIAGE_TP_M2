import os
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import glob
import cv2

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

# kmeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(X_train_image_flatten, y_train)
predictions = kmeans.predict(X_test_image_flatten)

# show how the KMeans algorithm separated our image into 2 new classes without knowing the 1 class (labels)
# here's class 0

pred_class_0 = np.where(predictions == 0)[0]
images_class_0 = [X_test[idx] for idx in pred_class_0]
nb_imgs_to_show = 10

fig = plt.figure(figsize=(50, 100))

for i in range(nb_imgs_to_show):
    fig.add_subplot(1, nb_imgs_to_show, i+1)
    image = cv2.imread(images_class_0[i])
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

plt.show()

# here's class 1
pred_class_1 = np.where(predictions == 1)[0]
images_class_1 = [X_test[idx] for idx in pred_class_1]
nb_imgs_to_show = 10

fig = plt.figure(figsize=(50, 100))

for i in range(nb_imgs_to_show):
    fig.add_subplot(1, nb_imgs_to_show, i+1)
    image = cv2.imread(images_class_1[i])
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

plt.show()
