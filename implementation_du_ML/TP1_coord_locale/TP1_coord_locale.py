# Hugo BERANGER - M2 MIAGE IA

from numba import cuda

@cuda.jit
def print_coord():
    print("block - thread :",cuda.blockIdx.x,cuda.blockIdx.y,cuda.blockIdx.z,cuda.threadIdx.x,cuda.threadIdx.y,cuda.threadIdx.z)

threadsperblock = 1             #size
threadim = threadsperblock,1,1  #dim
blockspergrid = 1
blocksdim = blockspergrid,1,1
#print_coord[blocksdim, threadim]()
cuda.synchronize()

print("==============================")
threadsperblock = 16             
threadim = threadsperblock,1,1  
blockspergrid = 1
blocksdim = blockspergrid,1,1
#print_coord[blocksdim, threadim]()
cuda.synchronize()

print("==============================")
threadsperblock = 1            
threadim = threadsperblock,1,1  
blockspergrid = 2
blocksdim = blockspergrid,1,1
#print_coord[blocksdim, threadim]()
cuda.synchronize()

print("==============================")
threadsperblock = 16           
threadim = 4,2,2  
blockspergrid = 1
blocksdim = blockspergrid,1,1
#print_coord[blocksdim, threadim]()
cuda.synchronize()
