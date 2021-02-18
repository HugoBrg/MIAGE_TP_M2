# Hugo BERANGER - M2 MIAGE IA

from numba import cuda
import numpy as np
from PIL import Image
import math


desired_width = 32
im = Image.open("dog.jpg")
print(im.format, im.size, im.mode)
wpercent = (desired_width/float(im.size[0]))
hsize = int((float(im.size[1])*float(wpercent)))
im = im.resize((desired_width,hsize), Image.ANTIALIAS)
im.show()

data = np.array(im)
newIm = cuda.device_array((32,32),dtype=np.uint8)

@cuda.jit
def bw(data,newIm):
    #print("block - thread :",cuda.blockIdx.x,cuda.blockIdx.y,cuda.blockIdx.z,cuda.threadIdx.x,cuda.threadIdx.y,cuda.threadIdx.z)
    x = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
    y = cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.y
    newIm[x,y] = np.uint8((0.3*data[y,x][0]) + (0.59*data[y,x][1]) + (0.11*data[y,x][2]))



threadim = 32,32,1
blocksdim = 1,1,1
data = cuda.to_device(data)
bw[blocksdim, threadim](data,newIm)
newIm.copy_to_host()
cuda.synchronize()

res = Image.fromarray(np.array(newIm))
res.show()