from numba import cuda
import numpy as np

@cuda.jit
def print_coord():
    print("block - thread :",cuda.blockIdx.x,cuda.blockIdx.y,cuda.blockIdx.z,cuda.threadIdx.x,cuda.threadIdx.y,cuda.threadIdx.z)

@cuda.jit
def device(an_array):
    print(cuda.grid(3)[2]+cuda.grid(3)[2]*cuda.grid(3)[0]+cuda.grid(3)[0]*cuda.grid(3)[1]*cuda.grid(3)[2])
    #print("pos : ",(cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x ),(cuda.threadIdx.y + cuda.blockIdx.y * cuda.blockDim.y),(cuda.threadIdx.z + cuda.blockIdx.z * cuda.blockDim.z))
    #print("block - thread :",cuda.blockIdx.x,cuda.blockIdx.y,cuda.blockIdx.z,cuda.threadIdx.x,cuda.threadIdx.y,cuda.threadIdx.z)

threadsperblock = 1             #size
threadim = threadsperblock,1,1  #dim
blockspergrid = 1
blocksdim = blockspergrid,1,1
print_coord[blocksdim, threadim]()
cuda.synchronize()

print("==============================")
threadsperblock = 16             
threadim = threadsperblock,1,1  
blockspergrid = 1
blocksdim = blockspergrid,1,1
print_coord[blocksdim, threadim]()
cuda.synchronize()

print("==============================")
threadsperblock = 1            
threadim = threadsperblock,1,1  
blockspergrid = 2
blocksdim = blockspergrid,1,1
print_coord[blocksdim, threadim]()
cuda.synchronize()

print("==============================")
threadsperblock = 16           
threadim = 4,2,2  
blockspergrid = 1
blocksdim = blockspergrid,1,1
#print_coord[blocksdim, threadim]()
cuda.synchronize()

print("==============================")
an_array = np.zeros(shape=(100))
for i in range (100):
    an_array[i] = i

threadsperblock = 16            
threadim = threadsperblock,3,3
blockspergrid = 1
blocksdim = blockspergrid,1,1
device[blocksdim, threadim](an_array)

