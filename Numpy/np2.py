#Slicing 1D and multi D numpy arrays

import numpy as np

oneDarray = np.array([1,2,3,4,5,6])

print(oneDarray[0:])
print(oneDarray[::-1])
print(oneDarray[-1:-3:-1])

MultiDarray = np.array([[1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12]])

print(MultiDarray[0,0]) #First element of the first dimension
print(MultiDarray[0:,0:]) #print everything
print(MultiDarray[0:3,0:2]) # first 2 element of all 3 dimesnion