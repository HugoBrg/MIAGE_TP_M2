# Hugo BERANGER - M2 MIAGE IA

from numba import cuda
import numpy as np

@cuda.jit
def device(an_array):
    #print(cuda.grid(3)[2]+cuda.grid(3)[2]*cuda.grid(3)[0]+cuda.grid(3)[0]*cuda.grid(3)[1]*cuda.grid(3)[2])  
    #print("pos : ",(cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x ),(cuda.threadIdx.y + cuda.blockIdx.y * cuda.blockDim.y),(cuda.threadIdx.z + cuda.blockIdx.z * cuda.blockDim.z))
    #print("block - thread :",cuda.blockIdx.x,cuda.blockIdx.y,cuda.blockIdx.z,cuda.threadIdx.x,cuda.threadIdx.y,cuda.threadIdx.z)

    #print(cuda.blockIdx.x *cuda.blockDim.x + cuda.threadIdx.x)     #1D1D

    blockId = cuda.blockIdx.x+ cuda.blockIdx.y * cuda.gridDim.x
    threadId = blockId * (cuda.blockDim.x * cuda.blockDim.y)+ (cuda.threadIdx.y * cuda.blockDim.x)+ cuda.threadIdx.x
    #print(threadId)                                                #2D2D

    pos = cuda.grid(2)
    print(pos[0],pos[1])

an_array = np.zeros(shape=(100))
for i in range (100):
    an_array[i] = i

threadsperblock = 16            
threadim = threadsperblock,1,1
blockspergrid = 2
blocksdim = blockspergrid,1,1
#device[blocksdim, threadim](an_array)

threadsperblock = 14            
threadim = int(threadsperblock/2),int(threadsperblock/2),1
blockspergrid = 4
blocksdim = int(blockspergrid/2),int(blockspergrid/2),1
#device[blocksdim, threadim](an_array)