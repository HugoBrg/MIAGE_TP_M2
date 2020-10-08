# Hugo BERANGER - M2 MIAGE IA

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
import glob
import pickle
import os
import cv2

#!wget --no-check-certificate -r 'http://www.i3s.unice.fr/~sanabria/files/dataset.zip' -O dataset.zip
#!unzip -qq dataset.zip -d /home/hugo/Documents/
#!ls /home/hugo/Documents/dataset
dataset_path = "/home/hugo/Documents/dataset/"

# Importation du dataset
all_classes = os.listdir(dataset_path)


# Personnes choisies pour la comparaison
person1 = 'Lucie_Bila'
person2 = 'Carlo_Conti'
chosen_classes = [person1, person2]

#-------------Affichage des personnes choisies-------------#

class_to_see = person1
path_files_per_class = glob.glob(dataset_path + class_to_see + "/*")
image_id_to_see = 100
image_path = path_files_per_class[image_id_to_see]

# Lecture de l'image
image = cv2.imread(image_path)
height, width, depth = image.shape

# Redimensionnage
new_size_rows = width*3
new_size_columns = height*3
new_image = cv2.resize(image, (new_size_rows, new_size_columns))
print(person1)
window_name = 'window'
cv2.imshow(window_name, new_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

class_to_see = person2
path_files_per_class = glob.glob(dataset_path + class_to_see + "/*")
image_path = path_files_per_class[image_id_to_see]

# Lecture de l'image
image = cv2.imread(image_path)
height, width, depth = image.shape

# Redimensionnage
new_size_rows = width*3
new_size_columns = height*3
new_image = cv2.resize(image, (new_size_rows, new_size_columns))
print(person2)
cv2.imshow(window_name, new_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

#---------------------------------------------------------#


# Récupération des chemins de nos images en X
X = []
for person1 in chosen_classes:
    class_path = dataset_path + person1
    for image_path in glob.glob(class_path + "/*.jpg"):
        X.append(image_path)

for person2 in chosen_classes:
    class_path = dataset_path + person2
    for image_path in glob.glob(class_path + "/*.jpg"):
        X.append(image_path)

# Association de chaque image à sa classe en Y
y = []
for image_path in X:
    y.append(image_path.split('/')[-2])

# On met des 0 à la place du nom de person1 et des 1 à la place du nom de person2
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)

# Séparations de nos datasets en 3 partie de respectivement 80%, 10% et 10%
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y)
X_test, X_val, y_test, y_val = train_test_split(
    X_test, y_test, test_size=0.5, stratify=y_test)

# Affichage ldu nombre de données dans chaque partie du dataset
print('training samples:', len(X_train))
print('testing samples:', len(X_test))
print('validation samples:', len(X_val))

# Affichage de la taille des 3 différents ensembles du dataset, l'entrainement, le test et la validation


def read_images(X):
    X_bw = []
    for image_path in X:
        # ... ## Read image in black and white
        image = cv2.imread(image_path, 0)
        X_bw.append(image)
    return np.asarray(X_bw)


X_train_bw = read_images(X_train)
X_test_bw = read_images(X_test)
X_val_bw = read_images(X_val)
