# Hugo BERANGER - M2 MIAGE IA

from numba import cuda
import numpy as np

@cuda.jit
def memoire_globale(array1,array2,array3):
    print("block - thread :",cuda.blockIdx.x,cuda.blockIdx.y,cuda.blockIdx.z,cuda.threadIdx.x,cuda.threadIdx.y,cuda.threadIdx.z)


threadsperblock = 16           
threadim = threadsperblock,1,1  
blockspergrid = 3
blocksdim = blockspergrid,1,1
array1 = np.int8()
array2 = np.int32()
array3 = np.float32()

#memoire_globale[blocksdim, threadim](array1,array2,array3)
cuda.synchronize()