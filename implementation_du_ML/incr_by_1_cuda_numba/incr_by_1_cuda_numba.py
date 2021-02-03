from numba import cuda
import numpy as np

@cuda.jit
def increment_by_one(an_array):
    pos = cuda.grid(1)
    if pos < an_array.size:
        an_array[pos] += 1

an_array = np.array([1,2,3])
print(an_array)

threadsperblock = 32
blockspergrid = (an_array.size + (threadsperblock - 1)) # threadsperblock
increment_by_one[blockspergrid, threadsperblock](an_array)

print(an_array)