# Hugo BERANGER - M2 MIAGE IA

# creating a new dataset
import pickle
import os
from google.colab.patches import cv2_imshow
import cv2
import glob


#!wget --no-check-certificate -r 'http://www.i3s.unice.fr/~sanabria/files/dataset.zip' -O dataset.zip
#!unzip -qq dataset.zip -d /home/hugo/Documents/
#!ls /home/hugo/Documents/dataset

dataset_path = "/home/hugo/Documents/dataset/"


new_dataset_path = "/home/hugo/Documents/new_dataset/"
try:
    os.mkdir(new_dataset_path)
except OSError:
    print("Creation of the directory %s failed" % new_dataset_path)
else:
    print("Successfully created the directory %s " % new_dataset_path)


dataset_extract = []
classes = os.listdir(dataset_path)
for class_name in classes:
    path_files_per_class = glob.glob(dataset_path + class_name + "/*")
    new_dataset_path = dataset_path + class_name

    try:
        os.mkdir("/home/hugo/Documents/new_dataset/" + class_name)
    except OSError:
        print("Creation of the directory %s failed" % new_dataset_path)
    else:
        print("Successfully created the directory %s " % new_dataset_path)

    files = []
    files.append(class_name)
    for f in range(len([f for f in os.listdir(new_dataset_path)if os.path.isfile(os.path.join(new_dataset_path, f))])):
        image_id_to_see = f
        image_path = path_files_per_class[image_id_to_see]
        files.append(cv2.imread(image_path))
    dataset_extract.append(files)


# loads the cascacade file for face detection
cascade_fn = cv2.data.haarcascades+"haarcascade_frontalface_alt.xml"


# creates the cascade classifier of the previous file
cascade = cv2.CascadeClassifier(cv2.samples.findFile(cascade_fn))


def detect(frame):
    # Each face is a tuple (x, y, w, h) where x,y is the top left corner of the recangle where the face is detected and w,h are the width and height of the rectangle.
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    # -- Detect faces
    faces = cascade.detectMultiScale(frame_gray)
    return faces


new_dataset = []
for files in dataset_extract:
    faces = []
    faces.append(files[0])
    for u in range(1, len(files)):
        faces_rects = detect(files[u])
        if len(faces_rects) > 0:
            f, y, w, h = faces_rects[0]  # Take the first face
            face = files[u][y: y + h, f: f + w]
            faces.append(face)
    new_dataset.append(faces)


os.chdir("/home/hugo/Documents/new_dataset/")


for files in new_dataset:
    for f in range(1, len(files)):
        os.chdir("/home/hugo/Documents/new_dataset/" + files[0])
        filename = str(f-1) + '.jpg'
        cv2.imwrite(filename, files[f])
