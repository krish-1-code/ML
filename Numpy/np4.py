#Shape and ReShape

import numpy as np

np1 = np.arange(1,13,1)
print(np1)
print(np1.shape)

np2 = np1.reshape(3,4) #3 rows 4 columns
print(np2)

#Two flatten the original array -> turning it into a 1D arary:

np3 = np2.reshape(-1)
print(np3)