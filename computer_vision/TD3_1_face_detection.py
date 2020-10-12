import cv2 as cv
from PIL import Image
from IPython.display import display, Javascript, HTML
from google.colab.output import eval_js, register_callback
from base64 import b64decode, b64encode
import io
import numpy as np

# using javascript to stream the webcam video
# create the window and stream the webcam on it
# async function can wait for Promise function to run
js = Javascript('''
  async function create(){
    div = document.createElement('div');

    video = document.createElement('video');
    video.setAttribute('playsinline', '');

    document.body.appendChild(div);
    div.appendChild(video);

    stream = await navigator.mediaDevices.getUserMedia({video: {facingMode: "environment"}});
    video.srcObject = stream;

    await video.play();

    canvas =  document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);

    div_out = document.createElement('div');
    document.body.appendChild(div_out);
    img = document.createElement('img');
    div_out.appendChild(img);

    //width and height of the image
    return [canvas.width, canvas.height]
    }

    async function capture(){
      return await new Promise(function(resolve, reject){
          pendingResolve = resolve;
          canvas.getContext('2d').drawImage(video, 0, 0);
          result = canvas.toDataURL('image/jpeg', 0.8);
          pendingResolve(result);
      })
    }
    function showimg(imgb64){
        img.src = "data:image/jpg;base64," + imgb64;
    }
    ''')

# conversion functions


def byte2image(byte):
    jpeg = b64decode(byte.split(',')[1])
    im = Image.open(io.BytesIO(jpeg))
    return np.array(im)


def image2byte(image):
    image = Image.fromarray(image)
    buffer = io.BytesIO()
    image.save(buffer, 'jpeg')
    buffer.seek(0)
    x = b64encode(buffer.read()).decode('utf-8')
    return x


# loads the cascacade file for face detection
cascade_fn = cv.data.haarcascades+"haarcascade_frontalface_alt.xml"

# creates the cascade classifier of the previous file
cascade = cv.CascadeClassifier(cv.samples.findFile(cascade_fn))


def detect(frame):
    # Each face is a tuple (x, y, w, h) where x,y is the top left corner of the recangle where the face is detected and w,h are the width and height of the rectangle.
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    # -- Detect faces
    faces = cascade.detectMultiScale(frame_gray)
    return faces


def display_faces(frame, faces):
    for (x, y, w, h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2),
                           0, 0, 360, (255, 0, 255), 4)
    return frame


display(js)
w, h = eval_js('create()')
while True:
    byte = eval_js('capture()')
    img = byte2image(byte)
    faces = detect(img)
    img = display_faces(img, faces)
    eval_js('showimg("{}")'.format(image2byte(img)))
